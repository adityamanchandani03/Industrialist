import streamlit as st

from services.integration import upload_document
from services.file_manager import (
    save_uploaded_file,
    delete_temp_file,
    allowed_file
)

st.set_page_config(
    page_title="Document Hub",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Document Hub")

st.write("Upload an industrial document for AI processing.")

uploaded_file = st.file_uploader(
    "Choose a PDF or Image",
    type=["pdf", "png", "jpg", "jpeg"]
)

if uploaded_file:

    if not allowed_file(uploaded_file.name):

        st.error("Unsupported file type.")

        st.stop()

    st.success("File uploaded successfully.")

    if st.button("🚀 Process Document"):

        with st.spinner("Processing document..."):

            temp_path = save_uploaded_file(uploaded_file)

            try:

                result = upload_document(temp_path)

                if result["status"] == "success":

                    st.session_state.processed = True

                    st.session_state.filename = result.get(
                        "filename",
                        ""
                    )

                    st.session_state.cleaned_text = result.get(
                        "cleaned_text",
                        ""
                    )

                    st.session_state.chunks = result.get(
                        "chunks",
                        []
                    )

                    st.session_state.entities = result.get(
                        "entities",
                        []
                    )

                    st.session_state.cloudinary_url = result.get(
                        "cloudinary_url",
                        ""
                    )

                    st.success("✅ Document processed successfully!")

                    st.info(
                        """
The document has been processed successfully.

You can now use:

• 🤖 AI Copilot

• 🏭 Asset 360

• 🛠 RCA Analysis
"""
                    )

                else:

                    st.error(result["message"])

            except Exception as e:

                st.error(f"Error: {str(e)}")

            finally:

                delete_temp_file(temp_path)