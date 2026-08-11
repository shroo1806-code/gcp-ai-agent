import os
from google import genai

# Initialize the standard Gemini client
# Streamlit will automatically use the GOOGLE_API_KEY from your Secrets
client = genai.Client()

# Start a chat session with the system instructions
chat = client.chats.create(
    model="gemini-2.0-flash",
    config={
        "system_instruction": "You are a helpful, enthusiastic AI assistant for the Arcade program. You always answer questions cheerfully and occasionally use arcade, gaming, or cloud computing puns."
    }
)

# Create a function that Streamlit can use
def run_agent(user_input):
    response = chat.send_message(user_input)
    return response.text
