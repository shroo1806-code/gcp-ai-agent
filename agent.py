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

print("=======================================")
print("👾 Arcade Agent is online! Type 'quit' to exit.")
print("=======================================")

# Start a chat session so the agent remembers conversation history
chat = model.start_chat()

while True:
    user_input = input("\nYou: ")
    if user_input.lower() == 'quit':
        print("Arcade Agent: Game Over! Thanks for playing. 🎮")
        break
    
    # Send the prompt to the Vertex AI API
    response = chat.send_message(user_input)
    print(f"Arcade Agent: {response.text}")
