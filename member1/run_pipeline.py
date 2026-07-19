import os

from member1.services.cloudinary_service import (
    upload_file,
    download_file,
    delete_temp_file
)

from member1.services.unifiedProcessor import process_document
from member1.services.text_cleaner import clean_text
from member1.services.text_chunker import create_chunks
from member1.services.entity_extractor import extract_entities
from member1.services.output_manager import (
    save_cleaned_text,
    save_chunks,
    save_entities
)


def run_pipeline(file_path):
    """
    Complete document processing pipeline.

    Uploads document to Cloudinary,
    downloads temporary copy,
    processes it,
    returns results.
    """

    print("\nUploading document to Cloudinary...")

    cloudinary_url = upload_file(file_path)

    print("Cloudinary URL:")
    print(cloudinary_url)

    print("\nDownloading temporary file...")

    temp_file = download_file(cloudinary_url)

    print("\nReading document...")

    text = process_document(temp_file)

    print("Cleaning text...")

    cleaned_text = clean_text(text)

    save_cleaned_text(cleaned_text)

    print("Creating chunks...")

    chunks = create_chunks(cleaned_text)

    save_chunks(chunks)

    print("Extracting entities...")

    entities = extract_entities(cleaned_text)

    save_entities(entities)

    delete_temp_file(temp_file)

    print("\nPipeline Completed Successfully!")

    return {

        "status": "success",

        "filename": os.path.basename(file_path),

        "cloudinary_url": cloudinary_url,

        "cleaned_text": cleaned_text,

        "chunks": chunks,

        "entities": entities

    }


if __name__ == "__main__":

    file_path = "member1/data/sample-doc/inspection_report.pdf"

    result = run_pipeline(file_path)

    print(result)