import streamlit as st
from vertexai.generative_models import GenerativeModel
import vertexai

# Initialize Vertex AI
vertexai.init(project="YOUR_PROJECT_ID", location="asia-south1")

# Load Gemini model
model = GenerativeModel("gemini-1.5-flash")

st.title("🤖 Shriyanshu's AI Agent")

user_input = st.text_input("Ask me anything:")

if st.button("Send"):
    if user_input:
        chat = model.start_chat()
        response = chat.send_message(user_input)
        st.write("**AI:**", response.text)
