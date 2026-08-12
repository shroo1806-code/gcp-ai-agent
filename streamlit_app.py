import streamlit as st
from agent import model  # import your Gemini model setup

st.title("🤖 Shriyanshu's AI Agent")

user_input = st.text_input("Ask me anything:")
if st.button("Send"):
    if user_input:
        chat = model.start_chat()
        response = chat.send_message(user_input)
        st.write("### Response:")
        st.write(response.text)
