# Chat AI Assistant

A simple chat application using Streamlit and LangChain with Ollama LLM (Llama 3) backend.

## Features

- Conversational AI assistant powered by Llama 3 via Ollama
- Maintains chat history and context
- User-friendly Streamlit web interface

## Requirements

- Python 3.8+
- pip

## Installation

1. Clone the repository:
   ```bash
   git clone git@github.com:varnie/chatai_assistant.git ./chatai
   cd ./chatai
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   
Make sure you have Ollama installed and running.

## Usage
1. Start the Ollama server:
   ```bash
   ollama serve
   ```
2. Run the Streamlit app:
   ```bash
    streamlit run chat_app.py
    ```
3. Open your web browser and go to `http://localhost:8501`

## Configuration

You can configure the LLM model by modifying the `model_name` variable in `chat_app.py`. By default, it uses `llama3`.