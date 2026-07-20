import os
from dotenv import load_dotenv
import google.generativeai as genai
from PIL import Image
import streamlit as st


load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    API_KEY = st.secrets["GEMINI_API_KEY"]

model = genai.GenerativeModel("gemini-1.5-flash")

# 



def extract_text_from_image(image_path):
    image = Image.open(image_path)

    response = model.generate_content([
        "Extract all text from this industrial document. Return only the extracted text.",
        image
    ])

    return response.texts
