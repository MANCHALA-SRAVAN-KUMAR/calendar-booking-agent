import streamlit as st
import requests

st.set_page_config(page_title="📅 Calendar Booking Chatbot", layout="centered")
st.title("📅 Calendar Booking Chatbot")
st.caption("Type messages like show me calendar, book slot, help, etc.")

def send_message(message):
    try:
        response = requests.post("http://127.0.0.1:8000/chat", json={"message": message})
        return response.json().get("response", "⚠️ No response from backend.")
    except Exception:
        return "⚠️ Backend did not respond."

if "messages" not in st.session_state:
    st.session_state.messages = []

for role, content in st.session_state.messages:
    with st.chat_message(role):
        st.markdown(content, unsafe_allow_html=True)

user_input = st.chat_input("Your message...")
if user_input:
    st.session_state.messages.append(("user", user_input))
    with st.chat_message("user"):
        st.markdown(user_input)

    response = send_message(user_input)
    if response.startswith("<h3>") or response.startswith("<h4>"):
        with st.chat_message("assistant"):
            st.markdown(response, unsafe_allow_html=True)
    else:
        st.session_state.messages.append(("assistant", response))
        with st.chat_message("assistant"):
            st.markdown(response)
