import vertexai
from vertexai.generative_models import GenerativeModel
import os

# Initialize Vertex AI with your project ID
vertexai.init(project="ai-agent-505218", location="us-central1")

# Load the Gemini model
model = GenerativeModel(
    "gemini-1.5-flash",
    system_instruction=[
        "You are a helpful, enthusiastic AI assistant for the Arcade program.",
        "You always answer questions cheerfully and occasionally use arcade, gaming, or cloud computing puns."
    ]
)

# Start a chat session
chat = model.start_chat()

# Create a function that Streamlit can use
def run_agent(user_input):
    response = chat.send_message(user_input)
    return response.text
