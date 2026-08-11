import streamlit as st
from google import genai

# Explicitly grab the API key from Streamlit Secrets
api_key = st.secrets["GOOGLE_API_KEY"]

# Initialize the client using that specific key
client = genai.Client(api_key=api_key)

# Start a chat session
chat = client.chats.create(
    model="gemini-1.5-flash",
    config={
        "system_instruction": "You are a helpful, enthusiastic AI assistant for the Arcade program. You always answer questions cheerfully and occasionally use arcade, gaming, or cloud computing puns."
    }
)

# Create a function that Streamlit can use
def run_agent(user_input):
    response = chat.send_message(user_input)
    return response.text
