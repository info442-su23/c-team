from langchain.prompts import (
    ChatPromptTemplate,
    PromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

label_prompt = "You are a helpful assistant that outputs concise labels for provided text chunks"
system_label_prompt = SystemMessagePromptTemplate.from_template(label_prompt)
chunk_label_prompt = "Give this chunk of text a label based on its content, use a few words, maximum a sentence: {text_chunk}"
human_label_prompt = HumanMessagePromptTemplate.from_template(chunk_label_prompt)

def label_chat_prompt():
    chat_prompt = ChatPromptTemplate.from_messages([system_label_prompt, human_label_prompt])
    #chat_prompt.format_prompt(text_chunk)
    return chat_prompt

table_contents_prompt = "You are a helpful assistant that outputs well-structured tables of contents from provided text chunk labels"
system_table_contents_prompt = SystemMessagePromptTemplate.from_template(table_contents_prompt)
label_table_contents_prompt = "Given these labels for chunks of a text (the text is a transcript of a lecture), produce a meaningful table of contents(feel free to integrate labels together and change the wording, the only thing you need to keep the same is the chronological order of original labels) (don't add links, they will be added later): {labels}"
human_table_contents_prompt = HumanMessagePromptTemplate.from_template(label_table_contents_prompt)

def table_contents_chat_prompt():
    chat_prompt = ChatPromptTemplate.from_messages([system_table_contents_prompt, human_table_contents_prompt])
    #chat_prompt.format_prompt(labels)
    return chat_prompt

summary_prompt = "You are a helpful assistant that outputs academically-styled study notes/summaries based on provided chunks of text from lectures"
system_summary_prompt = SystemMessagePromptTemplate.from_template(summary_prompt)
note_summary_prompt = "Summarize the following chunk of text, it's part of a lecture transcript - use bulletpoints and other techniques in your summary - it needs to retain the main academic information contained within it, your summary will be used by college students to study the topic discussed in lecture: {text_chunk}"
human_summary_prompt = HumanMessagePromptTemplate.from_template(note_summary_prompt)

def summary_chat_prompt():
    chat_prompt = ChatPromptTemplate.from_messages([system_summary_prompt, human_summary_prompt])
    #chat_prompt.format_prompt(text_chunk)
    return chat_prompt