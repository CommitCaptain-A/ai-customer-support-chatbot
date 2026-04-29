import streamlit as st
from app import ask_ai

st.set_page_config(page_title="Customer Support Chatbot", layout="centered")

st.title("💬 Customer Support Chatbot")
st.write("Ask any question related to our services.")

user_input = st.text_input("Enter your question:")

if st.button("Ask"):
    if user_input.strip():
        response = ask_ai(user_input)
        st.success(response)
    else:
        st.warning("Please enter a question.")