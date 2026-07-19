import os
import tempfile
import requests
import cloudinary
import cloudinary.uploader

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Cloudinary
cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET"),
)


def upload_file(file_path):
    """
    Upload a PDF/Image to Cloudinary.

    Returns:
        secure_url
    """

    result = cloudinary.uploader.upload(
    file_path,
    folder="industrialist",
    resource_type="raw"
)

    print("Uploaded Successfully")

    return result["secure_url"]


def download_file(secure_url):
    """
    Download Cloudinary file to a temporary location.

    Returns:
        Local file path
    """

    response = requests.get(secure_url)

    if response.status_code != 200:
        raise Exception("Unable to download file from Cloudinary")

    extension = secure_url.split(".")[-1]

    temp = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=f".{extension}"
    )

    temp.write(response.content)
    temp.close()

    print("Downloaded Successfully")

    return temp.name


def delete_temp_file(file_path):
    """
    Delete temporary downloaded file.
    """

    if os.path.exists(file_path):
        os.remove(file_path)
        print("Temporary file deleted.")