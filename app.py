
import streamlit as st # pyright: ignore[reportMissingImports]
from summarizer import load_summarizer, summarize_text

st.set_page_config(
    page_title="Text Summarization LLM",
    page_icon="📝",
    layout="wide"
)

st.title("Text Summarization LLM")
st.write("Convert long text into a short summary using Hugging Face AI.")

@st.cache_resource
def get_model():
    return load_summarizer()


text = st.text_area(
    "Enter your long text",
    height=300,
    placeholder="Paste your article or paragraph here..."
)

length = st.selectbox(
    "Choose summary length",
    ["Short", "Medium", "Long"]
)

if st.button("Generate Summary"):
    if not text.strip():
        st.warning("Please enter some text.")
    else:
        try:
            with st.spinner("Loading AI model... First time may take a few minutes."):
                model = get_model()

            with st.spinner("Summarizing your text..."):
                summary = summarize_text(text, model, length)

            st.subheader("Your Summary")
            st.write(summary)

            col1, col2 = st.columns(2)
            col1.metric("Original Words", len(text.split()))
            col2.metric("Summary Words", len(summary.split()))

            st.download_button(
                "Download Summary",
                data=summary,
                file_name="summary.txt",
                mime="text/plain"
            )

        except Exception as error:
            st.error(f"Error: {error}")
