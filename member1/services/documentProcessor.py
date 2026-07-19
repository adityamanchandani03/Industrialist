import fitz
import os
from PIL import Image

from member1.services.gemini_ocr import extract_text_from_image


def process_pdf(file_path):
    """
    Extract text from PDF.
    If a page has no selectable text, use Gemini OCR.
    """

    text = ""

    pdf = fitz.open(file_path)

    for page in pdf:

        extracted = page.get_text()

        if extracted.strip():

            text += extracted + "\n"

        else:

            pix = page.get_pixmap()

            temp_image = "temp_page.png"

            pix.save(temp_image)

            text += extract_text_from_image(temp_image) + "\n"

            os.remove(temp_image)

    pdf.close()

    return text