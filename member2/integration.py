"""
Member 2 Integration

Connects Member 1 and Member 2
"""

import sys
import os

# Add project root to Python path
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

if ROOT not in sys.path:
    sys.path.append(ROOT)

from member1.run_pipeline import run_pipeline

from member2.services.embedding_service import create_embeddings
from member2.services.chroma_service import store_chunks
from member2.services.knowledge_graph import build_graph
from member2.services.rag_pipeline import ask_question


def process_document(file_path):

    print("\nRunning Member 1 Pipeline...\n")

    result = run_pipeline(file_path)

    if result["status"] != "success":
        return result

    chunks = result["chunks"]
    entities = result["entities"]

    print("\nCreating Embeddings...")

    embeddings = create_embeddings(chunks)

    print("\nSaving into ChromaDB...")

    store_chunks(chunks, embeddings)

    print("\nBuilding Knowledge Graph...")

    build_graph(entities)

    return {

        "status": "success",

        "filename": result["filename"],

        "cloudinary_url": result["cloudinary_url"],

        "cleaned_text": result["cleaned_text"],

        "chunks": result["chunks"],

        "entities": result["entities"]

    }


def ask(question):

    return ask_question(question)