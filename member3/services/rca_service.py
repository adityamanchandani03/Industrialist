import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Read API key from .env (local) or Streamlit Secrets (cloud)
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    API_KEY = st.secrets["GEMINI_API_KEY"]

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_rca(document_text):

    prompt = f"""
You are an Industrial AI Engineer.

Analyze the following industrial inspection report.

Return the response in this format.

Root Cause:

Risk Level:

Immediate Action:

Long Term Recommendation:

Preventive Maintenance:

Summary:

Report:

{document_text}
"""

    response = model.generate_content(prompt)

    return response.text
