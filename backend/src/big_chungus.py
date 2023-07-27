def split_text_into_chunks(text, chunk_size=7000, percent=0.1):
    """
    Splits a text string into chunks of chunk_size characters with percent overlap.

    Args:
    - text: The input text string.
    - chunk_size: The desired chunk size. Default is 512.
    - percent: The percentage of overlap between adjacent chunks. Default is 0.1.

    Returns:
    - A list of text chunks.
    """
    """TODO
    more sophisticated sentence boundary detection, 
    consider using a Natural Language Processing library 
    such as NLTK or Spacy.
    """
    overlap = int(chunk_size * percent)
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        if end > len(text):
            end = len(text)
        chunk = text[start:end]

        # Find the last occurrence of a period in the chunk and slice the string up to that point
        #last_period_index = chunk.rfind('.')
        #if last_period_index != -1:
            #chunk = chunk[:last_period_index+1]

        chunks.append(chunk)
        start += chunk_size - overlap
        if start < 0:
            start = 0
    return chunks

if __name__ == "__main__":
    file = open('../text.txt', 'r')
    text = file.read()
    file.close()
    chunks = split_text_into_chunks(text)
    for chunk in chunks:
        print(f"\n\n\n{chunk}")
