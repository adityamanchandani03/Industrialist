"""
RAG Pipeline

1. Create embedding for user question.
2. Search similar chunks in ChromaDB.
3. Build context.
4. Ask Gemini.
"""

from member2.services.embedding_service import create_embedding
from member2.services.chroma_service import search_chunks
from member2.services.llm_service import generate_answer


def ask_question(question):
    """
    Answer questions using RAG.
    """

    print("\nSearching relevant document chunks...")

    # Create embedding for question
    query_embedding = create_embedding(question)

    # Search in ChromaDB
    results = search_chunks(query_embedding)

    documents = results["documents"][0]

    if len(documents) == 0:

        return {
            "status": "error",
            "message": "No relevant document found."
        }

    context = "\n\n".join(documents)

    print("\nContext Retrieved:\n")
    print(context)

    answer = generate_answer(question, context)

    return {
        "status": "success",
        "question": question,
        "context": context,
        "answer": answer
    }