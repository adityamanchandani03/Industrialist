"""
LLM Service

Uses Google Gemini to answer questions
based on document context.
"""

import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Read API key from .env (local) or Streamlit Secrets (cloud)
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    API_KEY = st.secrets["GEMINI_API_KEY"]

# Configure Gemini using the correct key
genai.configure(api_key=API_KEY)

# Create model
model = genai.GenerativeModel("gemini-1.5-flash")


def generate_answer(question, context):
    """
    Generate answer using retrieved document context.
    """

    prompt = f"""
You are an AI Industrial Document Assistant.

Answer ONLY from the given context.

If the answer is not available, reply exactly:

"I couldn't find this information in the uploaded documents."

------------------------
Context

{context}

------------------------

Question:

{question}

Answer:
"""

    response = model.generate_content(prompt)

    return response.text
