import streamlit as st
from chatbot import HealthChatbot

st.title("Nigerian Healthcare Assistant Chatbot")
st.write("Describe your symptoms and I will help you decide what to do.")

if "chatbot" not in st.session_state:
    st.session_state.chatbot = HealthChatbot()

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_input = st.chat_input("Describe your symptoms here...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    response = st.session_state.chatbot.chat(user_input)

    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.write(response)