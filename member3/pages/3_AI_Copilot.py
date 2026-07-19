import streamlit as st
from services.integration import ask_ai

st.set_page_config(page_title="AI Copilot", page_icon="🤖")

st.title("🤖 AI Copilot")
st.write("Ask questions from all uploaded industrial documents.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
question = st.chat_input("Ask a question about your documents...")

if question:

    # Show user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    # Generate answer
    with st.chat_message("assistant"):

        with st.spinner("Searching documents..."):

            try:

                result = ask_ai(question)

                if result["status"] == "success":

                    answer = result["answer"]

                    st.markdown(answer)

                    with st.expander("Retrieved Context"):

                        st.write(result["context"])

                else:

                    answer = result["message"]

                    st.error(answer)

            except Exception as e:

                answer = str(e)

                st.error(answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

st.divider()

if st.button("🗑 Clear Chat"):

    st.session_state.messages = []

    st.rerun()