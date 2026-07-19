def create_chunks(text, chunk_size=300, overlap=50):
    """
    Split text into overlapping chunks for RAG.
    """

    words = text.split()
    chunks = []
    start = 0

    while start < len(words):
        end = start + chunk_size
        chunk = " ".join(words[start:end])
        chunks.append(chunk)

        # Move forward but keep overlap
        start += chunk_size - overlap

    return chunks