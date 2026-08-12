import os
import vertexai
from vertexai.generative_models import GenerativeModel

# Get GCP configuration from environment variables
project_id = os.getenv("ai-agent-505218")
location = os.getenv("GCP_LOCATION", "us-central1")

# Initialize Vertex AI with project ID
vertexai.init(project=project_id, location=location)

# Load the model (Note: Ensure the model name matches GCP's standard naming, e.g., gemini-1.5-flash)
model = GenerativeModel(
    "gemini-1.5-flash",
    system_instruction=[
        "You are a helpful, enthusiastic AI assistant for the Arcade program.",
        "You always answer questions cheerfully and occasionally use arcade, gaming, or cloud computing puns."
    ]
)
print("=======================================")
print("👾 My AI Agent is online! Type 'quit' to exit.")
print("=======================================")

# Start a chat session so the agent remembers conversation history
chat = model.start_chat()

while True:
    user_input = input("\nYou: ")
    if user_input.lower() == 'quit':
        print("AI Agent: Game Over! Thanks for playing. 🎮")
        break
    
    # Send the prompt to the Vertex AI API
    response = chat.send_message(user_input)
    print(f"Arcade Agent: {response.text}")
