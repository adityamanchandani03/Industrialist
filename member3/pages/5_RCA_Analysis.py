import streamlit as st
import os

from services.rca_service import generate_rca

OUTPUT_FILE = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "../../member1/output/cleaned_text.txt"
    )
)

st.set_page_config(
    page_title="RCA Analysis",
    page_icon="🛠"
)

st.title("🛠 AI Root Cause Analysis")

if not os.path.exists(OUTPUT_FILE):

    st.warning("No processed document found.")

    st.stop()

with open(OUTPUT_FILE, "r", encoding="utf-8") as f:

    report = f.read()

st.subheader("Industrial Report")

st.text_area(
    "",
    report,
    height=250
)

if st.button("Generate AI RCA"):

    with st.spinner("Analyzing report..."):

        result = generate_rca(report)

    st.success("Analysis Completed")

    st.markdown(result)