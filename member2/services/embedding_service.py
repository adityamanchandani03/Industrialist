"""
Embedding Service

Converts text into vector embeddings using
Sentence Transformers.
"""

from sentence_transformers import SentenceTransformer

print("Loading embedding model...")

# Load model only once
model = SentenceTransformer("all-MiniLM-L6-v2")

print("Embedding model loaded successfully!")


def create_embedding(text: str):
    """
    Convert a single text string into an embedding vector.
    """

    embedding = model.encode(text)

    return embedding.tolist()

def create_embeddings(chunks):
    """
    Convert document chunks into embedding vectors.

    Supports:
    1. List[str]
    2. List[{"text": "..."}]
    """

    embeddings = []

    for chunk in chunks:

        if isinstance(chunk, dict):
            text = chunk["text"]
        else:
            text = chunk

        vector = create_embedding(text)

        embeddings.append(vector)

    return embeddings