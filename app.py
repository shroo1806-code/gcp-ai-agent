import streamlit as st
import agent # Imports your agent.py logic

st.title("🤖 My GCP AI Agent")
st.write("Type a message below to talk to my AI agent!")

# User input field
user_prompt = st.text_input("Enter your prompt:")

if st.button("Send") and user_prompt:
    with st.spinner("Agent is thinking..."):
        try:
            # Call your agent function from agent.py
            response = agent.run_agent(user_prompt) 
            st.success("Response:")
            st.write(response)
        except Exception as e:
            st.error(f"Error: {e}")
