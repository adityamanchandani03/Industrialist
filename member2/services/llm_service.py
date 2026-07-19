"""
LLM Service

Uses Google Gemini to answer questions
based on document context.
"""

import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_answer(question, context):
    """
    Generate answer using retrieved document context.
    """

    prompt = f"""
You are an AI Industrial Document Assistant.

Answer ONLY from the given context.

If the answer is not available,
reply:

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