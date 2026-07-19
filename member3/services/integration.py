"""
Member 3 Integration Service

Connects Streamlit UI with Member 2.
"""

import sys
import os

ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../..")
)

if ROOT not in sys.path:
    sys.path.append(ROOT)

from member2.integration import process_document, ask


def upload_document(file_path):
    """
    Upload and process document.
    """
    return process_document(file_path)


def ask_ai(question):
    """
    Ask AI from processed documents.
    """
    return ask(question)