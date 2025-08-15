import streamlit as st
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
You are a helpful assistant. Answer the user's questions as accurately as possible.
Here's the conversation history: {context}
User: {input}
Assistant:
"""

# Load model and tokenizer (cached)
@st.cache_resource
def load_model():
    return OllamaLLM(model="llama3")

model = load_model()
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

# Streamlit UI
st.title("Chat AI Assistant")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
if "context" not in st.session_state:
    st.session_state.context = ""

# Display chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User input
user_input = st.chat_input("Type your message here...")
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    if model:
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                # Generate response
                result = chain.invoke({"context": st.session_state.context, "input": user_input})
                ai_reply = result.strip()
                st.write(ai_reply)
                st.session_state.messages.append({"role": "assistant", "content": ai_reply})

                # Update chat context
                st.session_state.context += f"User: {user_input}\nAssistant: {ai_reply}\n"
    else:
        st.error("AI model not loaded!")

    # Clear the input field and rerun the app
    st.session_state.input = ""
