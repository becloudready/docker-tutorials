import streamlit as st
import openai

# Default backend URL
DEFAULT_BACKEND_URL = "http://localhost:11434/v1"

# UI for setting the backend URL
st.title("Chatbot using Ollama")
st.sidebar.header("Settings")
backend_url = st.sidebar.text_input("Backend URL", DEFAULT_BACKEND_URL)

# Initialize OpenAI client with user-defined backend URL
client = openai.OpenAI(base_url=backend_url)

# Chat session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Ask something..."):
    # Add user message to session state
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Call the backend API
    try:
        response = client.chat.completions.create(
            model="llama3.2:1b",  # Change this based on available models
            messages=st.session_state.messages
        )
        reply = response.choices[0].message.content
    except Exception as e:
        reply = f"Error: {e}"
    
    # Display assistant response
    with st.chat_message("assistant"):
        st.markdown(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})
