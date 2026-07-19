from google import genai
from dotenv import load_dotenv
import os
from PIL import Image

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def extract_text_from_image(image_path):

    image = Image.open(image_path)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            "Extract all text from this industrial document. Return only the extracted text.",
            image
        ]
    )

    return response.text