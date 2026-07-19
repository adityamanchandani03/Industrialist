import os
import cloudinary
import cloudinary.uploader
from dotenv import load_dotenv

load_dotenv()

cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET"),
    secure=True
)


def upload_file(file_path):
    """
    Upload a file to Cloudinary.

    Returns:
        dict containing secure_url, public_id, original_filename
    """

    try:
        response = cloudinary.uploader.upload(
            file_path,
            resource_type="auto"
        )

        return {
            "success": True,
            "secure_url": response["secure_url"],
            "public_id": response["public_id"],
            "original_filename": response["original_filename"]
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }


def delete_file(public_id):
    try:
        cloudinary.uploader.destroy(public_id, resource_type="raw")
        return True
    except:
        return False