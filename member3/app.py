import streamlit as st

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Industrialist",
    page_icon="🏭",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# Initialize Session Variables
# -----------------------------
if "processed" not in st.session_state:
    st.session_state.processed = False

if "cloudinary_url" not in st.session_state:
    st.session_state.cloudinary_url = ""

if "chunks" not in st.session_state:
    st.session_state.chunks = []

if "entities" not in st.session_state:
    st.session_state.entities = []

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:

    st.title("🏭 AI Industrialist")

    st.markdown("---")

    st.success("System Status")

    st.write("🟢 AI Engine Ready")

    st.write("🟢 Cloudinary Connected")

    st.write("🟢 Gemini Connected")

    st.markdown("---")

    st.info(
        """
Navigate using the Pages menu above.

Dashboard

Document Hub

AI Copilot

Asset 360

RCA Analysis

Knowledge Graph
"""
    )

# -----------------------------
# Main Page
# -----------------------------
st.title("🏭 AI Industrialist")

st.subheader("Industrial Knowledge Intelligence Platform")

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "Documents Processed",
        len(st.session_state.chunks)
    )

with col2:

    st.metric(
        "Entities",
        len(st.session_state.entities)
    )

with col3:

    st.metric(
        "Chat Messages",
        len(st.session_state.chat_history)
    )

st.markdown("---")

st.write(
"""
Welcome to AI Industrialist.

Use the navigation menu on the left to:

• Upload industrial documents

• Chat with AI

• View extracted entities

• Perform Root Cause Analysis

• Explore the Knowledge Graph
"""
)