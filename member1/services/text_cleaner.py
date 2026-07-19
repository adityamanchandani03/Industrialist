import re

def clean_text(text):
    """Clean extracted text before AI processing."""

    # Remove page markers like --- Page 1 ---
    text = re.sub(r"--- Page \d+ ---", " ", text)

    # Remove multiple spaces
    text = re.sub(r"\s+", " ", text)

    # Remove multiple blank lines
    text = re.sub(r"\n+", "\n", text)

    # Remove tabs
    text = text.replace("\t", " ")

    # Remove unnecessary symbols
    text = text.replace("•", "")
    text = text.replace("■", "")

    return text.strip()