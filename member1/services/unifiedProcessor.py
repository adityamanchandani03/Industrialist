import os

from member1.services.documentProcessor import process_pdf
from member1.services.gemini_ocr import extract_text_from_image


def process_document(file_path):
    """
    Process any supported document.

    Supported formats:
    - PDF
    - PNG
    - JPG
    - JPEG
    """

    extension = os.path.splitext(file_path)[1].lower()

    if extension == ".pdf":
        return process_pdf(file_path)

    elif extension in [".png", ".jpg", ".jpeg"]:
        return extract_text_from_image(file_path)

    else:
        raise Exception(f"Unsupported file format: {extension}")