import streamlit as st
import requests

# Set up page config
st.set_page_config(page_title="📅 Calendar Booking Chatbot", layout="centered")
st.title("📅 Calendar Booking Chatbot")
st.caption("Type messages like show me calendar, book slot, help, etc.")

# Function to send message to backend (Render URL)
def send_message(message):
    try:
        response = requests.post(
            "https://calendar-booking-agent-cyow.onrender.com/chat",  # <-- Updated backend URL
            json={"message": message}
        )
        return response.json().get("response", "⚠️ No response from backend.")
    except Exception:
        return "⚠️ Backend did not respond."

# Initialize message history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display past messages
for role, content in st.session_state.messages:
    with st.chat_message(role):
        st.markdown(content, unsafe_allow_html=True)

# Get user input
user_input = st.chat_input("Your message...")
if user_input:
    st.session_state.messages.append(("user", user_input))
    with st.chat_message("user"):
        st.markdown(user_input)

    # Get response from backend
    response = send_message(user_input)
    st.session_state.messages.append(("assistant", response))

    with st.chat_message("assistant"):
        st.markdown(response, unsafe_allow_html=True)
