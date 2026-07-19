import streamlit as st


def initialize_session():

    defaults = {

        "processed": False,

        "cloudinary_url": "",

        "chunks": [],

        "entities": [],

        "chat_history": [],

        "cleaned_text": "",

        "filename": ""

    }

    for key, value in defaults.items():

        if key not in st.session_state:

            st.session_state[key] = value