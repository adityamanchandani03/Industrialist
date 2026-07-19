import os
import json

OUTPUT_FOLDER = "output"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)


def save_cleaned_text(text):

    with open(
        os.path.join(OUTPUT_FOLDER, "cleaned_text.txt"),
        "w",
        encoding="utf-8"
    ) as file:

        file.write(text)


def save_chunks(chunks):

    with open(
        os.path.join(OUTPUT_FOLDER, "chunks.json"),
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(chunks, file, indent=4)


def save_entities(entities):

    with open(
        os.path.join(OUTPUT_FOLDER, "entities.json"),
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(entities, file, indent=4)