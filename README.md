
# Text Summarization LLM

A text summarization application built with Python, Streamlit, and Hugging Face Transformers.

## Features

- Summarizes long text into shorter content
- Short, medium, and long summary options
- Displays original and summary word counts
- Downloads summaries as text files
- Processes long input in smaller chunks

## Model

sshleifer/distilbart-cnn-12-6

## Technologies

- Python
- Streamlit
- Hugging Face Transformers
- PyTorch

## Installation

Install the required dependencies:

    python -m pip install -r requirements.txt

## Run the Application

    python -m streamlit run app.py --server.port 8505

The application will be available at http://localhost:8505.

The model requires an internet connection for its initial download.
