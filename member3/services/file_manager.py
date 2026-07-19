import os
import tempfile


ALLOWED_EXTENSIONS = [
    ".pdf",
    ".png",
    ".jpg",
    ".jpeg"
]


def allowed_file(filename):

    extension = os.path.splitext(filename)[1].lower()

    return extension in ALLOWED_EXTENSIONS


def save_uploaded_file(uploaded_file):

    extension = os.path.splitext(uploaded_file.name)[1]

    temp = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=extension
    )

    temp.write(uploaded_file.getbuffer())

    temp.close()

    return temp.name


def delete_temp_file(path):

    if os.path.exists(path):

        os.remove(path)