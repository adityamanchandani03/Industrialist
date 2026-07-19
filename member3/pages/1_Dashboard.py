import streamlit as st
from services.system_status import get_status

st.set_page_config(
    page_title="Dashboard",
    page_icon="🏭",
    layout="wide"
)

status = get_status()

# ----------------------------------------------------
# Header
# ----------------------------------------------------

st.title("🏭 Unified Asset & Operations Brain")

st.subheader(
    "AI-Powered Industrial Knowledge Intelligence Platform"
)

st.markdown("---")

# ----------------------------------------------------
# Welcome
# ----------------------------------------------------

st.markdown("""
Welcome to the **Unified Asset & Operations Brain**, an AI-powered platform designed to help industries process technical documents, search knowledge intelligently, analyze assets, and generate Root Cause Analysis (RCA).

### Core Modules

- 📄 Document Hub
- 🤖 AI Copilot
- 🏭 Asset 360
- 🛠 Root Cause Analysis
""")

st.markdown("---")

# ----------------------------------------------------
# Platform Overview
# ----------------------------------------------------

st.header("📊 Platform Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "AI Engine",
        "Gemini"
    )

with col2:
    st.metric(
        "Vector Database",
        "ChromaDB"
    )

with col3:
    st.metric(
        "Cloud Storage",
        "Cloudinary"
    )

st.markdown("---")

# ----------------------------------------------------
# Live System Status
# ----------------------------------------------------

st.header("🖥 Live System Status")

left, right = st.columns(2)

with left:

    if status["gemini"]:
        st.success("🟢 Gemini API Configured")
    else:
        st.error("🔴 Gemini API Not Configured")

    if status["cloudinary"]:
        st.success("🟢 Cloudinary Configured")
    else:
        st.error("🔴 Cloudinary Not Configured")

with right:

    if status["chromadb"]:
        st.success("🟢 ChromaDB Available")
    else:
        st.error("🔴 ChromaDB Not Available")

    if status["document"]:
        st.success("🟢 Document Processed")
    else:
        st.warning("🟡 No Document Processed Yet")

st.markdown("---")

# ----------------------------------------------------
# Features
# ----------------------------------------------------

st.header("🚀 Platform Features")

col1, col2 = st.columns(2)

with col1:

    st.info("""
### 📄 Document Hub

• Upload PDF/Image

• OCR & Text Extraction

• Cloud Storage

• AI Processing
""")

    st.success("""
### 🤖 AI Copilot

• Ask Questions

• Semantic Search

• RAG Pipeline

• Gemini Responses
""")

with col2:

    st.warning("""
### 🏭 Asset 360

• Equipment Details

• Inspection Summary

• Maintenance Information
""")

    st.error("""
### 🛠 RCA Analysis

• Root Cause

• Risk Level

• Recommendations

• Preventive Maintenance
""")

st.markdown("---")

# ----------------------------------------------------
# Workflow
# ----------------------------------------------------

st.header("🔄 Workflow")

st.markdown("""
1️⃣ Upload an industrial document using **Document Hub**

⬇️

2️⃣ AI extracts text and processes the document

⬇️

3️⃣ Embeddings are generated and stored in **ChromaDB**

⬇️

4️⃣ Ask questions using **AI Copilot**

⬇️

5️⃣ View **Asset 360** and generate **Root Cause Analysis**
""")

st.markdown("---")

# ----------------------------------------------------
# Technology Stack
# ----------------------------------------------------

st.header("🛠 Technology Stack")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
### Backend

- Python

- Streamlit

- ChromaDB
""")

with col2:
    st.markdown("""
### Artificial Intelligence

- Google Gemini

- Sentence Transformers

- Retrieval-Augmented Generation (RAG)
""")

with col3:
    st.markdown("""
### Cloud Services

- Cloudinary

- Render
""")

st.markdown("---")

# ----------------------------------------------------
# Footer
# ----------------------------------------------------

st.caption(
    "Unified Asset & Operations Brain | AI Industrial Knowledge Intelligence Platform"
)