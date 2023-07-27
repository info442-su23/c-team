from langchain.embeddings import HuggingFaceInstructEmbeddings, OpenAIEmbeddings
from langchain.vectorstores import Pinecone, Chroma
from types import SimpleNamespace


open_ai_embedder = OpenAIEmbeddings(model='text-embedding-ada-002')

"""
Messages - array of AI messages to embed
Message_id_name - type of embedding to store - label, summary, etc.
Text_name - name of the file to store
Embedder - which embeddings to use
Vector_store - which db to use
"""
#For databases that store metadata + embeddings in a single dict e.g. Pinecone
def embed(messages, message_id_name, text_name, embedder=open_ai_embedder, **kwargs):
    embeddings_dict = {f"{message_id_name}_{i}": {"embedding": embedding, "text": text_name, "type": message_id_name}
                       for i, embedding in enumerate(embedder.embed_documents(messages))}

    if message_id_name == "summary":
        labels = kwargs.get("labels", [None] * len(messages))
        for i, message_id in enumerate(embeddings_dict):
            embeddings_dict[message_id]["label"] = labels[i]

    return embeddings_dict

#For databases that store metadata and embeddings as separate lists
def embed_meta_separate(messages, message_id_name, text_name, embedder=open_ai_embedder, **kwargs):
    embeddings_list = [embedding for i, embedding in enumerate(embedder.embed_documents(messages))]
    metadatas = [{"text": text_name, "type": message_id_name, "id":f"{message_id_name}_{i}"} for i, _ in enumerate(messages)]

    if message_id_name == "summary":
        labels = kwargs.get("labels", [None] * len(messages))
        for i, _ in enumerate(messages):
            metadatas[i]["label"] = labels[i]
    
    return {"embeddings":embeddings_list, "metadatas":metadatas}



def store(embeddings_dict, text_name, vector_store=None):
    if(not vector_store):
        vector_store = Pinecone(index_name=text_name)
    elif(isinstance(vector_store, Chroma)):
        #LangChain bs workaround
        #TODO commit to LangChain to fix it
        vector_store._embedding_function = SimpleNamespace(embed_documents=lambda a:a)
        #vector_store._embedding_function.embed_documents = lambda a: a
        vector_store.add_texts(embeddings_dict["embeddings"], embeddings_dict["metadatas"])
    else:
        vector_store.add(embeddings_dict)

def retrieve(text_name=None, message_id_name=None, label=None, vector_store=None):
    if not vector_store:
        vector_store = Pinecone(index_name=text_name if text_name else "default_index")
    # Fetch all embeddings from the vector store
    all_embeddings = vector_store.fetch_all()
    # Filter the embeddings based on message_id_name and label
    filtered_embeddings = {message_id: data for message_id, data in all_embeddings.items()
                           if (not message_id_name or data["type"] == message_id_name) and 
                              (not label or data.get("label") == label)}
    # Transform embeddings back into text
    transformed_texts = {message_id: vector_store.decode(embedding["embedding"]) for message_id, embedding in filtered_embeddings.items()}
    
    return transformed_texts


def semantic_search(query, text_name=None, message_id_name=None, label=None, vector_store=None, embedder=open_ai_embedder):
    if not vector_store:
        vector_store = Pinecone(index_name=text_name if text_name else "default_index")
    # Create an embedding for the query
    query_embedding = embedder.embed([query])[0]
    # Create a VectorStoreRetriever
    retriever = vector_store.as_retriever()
    # Perform a semantic search in the vector store
    search_results = retriever.get_relevant_documents(query_embedding, top_k=10)
    # Filter the embeddings based on message_id_name and label
    filtered_results = {message_id: data for message_id, data in search_results.items()
                        if (not message_id_name or data["type"] == message_id_name) and 
                           (not label or data.get("label") == label)}
    # Transform embeddings back into text
    transformed_texts = {message_id: vector_store.decode(embedding["embedding"]) for message_id, embedding in filtered_results.items()}
    return transformed_texts

