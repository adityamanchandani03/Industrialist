import os
import chromadb
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()


def check_gemini():

    try:

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            return False

        genai.configure(api_key=api_key)

        return True

    except Exception:

        return False


def check_cloudinary():

    cloud = os.getenv("CLOUDINARY_CLOUD_NAME")
    key = os.getenv("CLOUDINARY_API_KEY")
    secret = os.getenv("CLOUDINARY_API_SECRET")

    return all([cloud, key, secret])


def check_chromadb():

    try:

        client = chromadb.PersistentClient(path="member2/database")

        client.heartbeat()

        return True

    except Exception:

        return False


def check_document():

    return os.path.exists("member1/output/cleaned_text.txt")


def get_status():

    return {

        "gemini": check_gemini(),

        "cloudinary": check_cloudinary(),

        "chromadb": check_chromadb(),

        "document": check_document()

    }