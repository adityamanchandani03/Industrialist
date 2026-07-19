import os
from dotenv import load_dotenv
import google.generativeai as genai
from PIL import Image

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")


def extract_text_from_image(image_path):
    image = Image.open(image_path)

    response = model.generate_content([
        "Extract all text from this industrial document. Return only the extracted text.",
        image
    ])

    return response.texts