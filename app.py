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
with st.sidebar:
    st.title("About")
    st.write("This AI assistant helps everyday Nigerians understand their systoms and decide what to do.")

    st.divider()

    st.title("How to Use")
    st.write("1. Describe your symptoms in English or Pidgin")
    st.write("2. Answer the follow up questions")
    st.write("3. Receive your health assessment")

    st.divider()

    st.title("Disclaimer")
    st.write("This is not a medical diagnosis. Always consult a qualified doctor for proper medical advice")

    st.divider()

    st.title("Built by")
    st.write("Benjamin Osezua")
    st.write("AI Developer | Python & Streamlit") 