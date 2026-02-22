import streamlit as st
from backend.chat_service import ChatService
from utils.session_manager import SessionManager

st.set_page_config(page_title="Mental Health Support Chatbot", layout="centered")

st.title("🧠 Mental Health Support Assistant")
st.caption("Confidential • Compassionate • Context-Aware")

SessionManager.initialize()
chat_service = ChatService()

# Display previous chat
for message in SessionManager.get_history():
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_input = st.chat_input("How are you feeling today?")

if user_input:
    SessionManager.add_message("user", user_input)

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = chat_service.get_response(
                SessionManager.get_history()
            )
            st.markdown(response)

    SessionManager.add_message("assistant", response)

# Clear conversation button
if st.button("Clear Conversation"):
    SessionManager.clear()
    st.rerun()