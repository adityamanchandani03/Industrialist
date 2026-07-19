"""
ChromaDB Service

Stores document chunks and embeddings.
Retrieves relevant chunks for RAG.
"""

import chromadb

# Create persistent database
client = chromadb.PersistentClient(path="member2/database")

collection = client.get_or_create_collection(
    name="industrial_documents"
)


def store_chunks(chunks, embeddings):
    """
    Store chunks into ChromaDB.
    """

    ids = []

    documents = []

    metadatas = []

    for i, chunk in enumerate(chunks):

        ids.append(str(i))

        # Handles both string chunks and dict chunks
        if isinstance(chunk, dict):
            documents.append(chunk["text"])
        else:
            documents.append(chunk)

        metadatas.append({
            "chunk_id": i
        })

    collection.add(
        ids=ids,
        documents=documents,
        embeddings=embeddings,
        metadatas=metadatas
    )

    print(f"{len(documents)} chunks stored in ChromaDB.")


def search_chunks(query_embedding, top_k=3):
    """
    Search similar chunks.
    """

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    return results