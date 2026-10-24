from transformers import pipeline # pyright: ignore[reportMissingImports]

MODEL_NAME = "sshleifer/distilbart-cnn-6-6"


def load_summarizer():
    return pipeline(
        "summarization",
        model=MODEL_NAME
    )


def summarize_text(text, summarizer, length="Medium"):
    if not text.strip():
        return ""

    settings = {
        "Short": (20, 60),
        "Medium": (40, 100),
        "Long": (80, 150)
    }

    min_length, max_length = settings[length]
    tokenizer = summarizer.tokenizer

    token_ids = tokenizer.encode(
        text,
        add_special_tokens=False
    )

    chunk_size = 700
    chunks = [
        token_ids[i:i + chunk_size]
        for i in range(0, len(token_ids), chunk_size)
    ]

    summaries = []

    for chunk in chunks:
        chunk_text = tokenizer.decode(
            chunk,
            skip_special_tokens=True
        )

        if not chunk_text.strip():
            continue

        result = summarizer(
            chunk_text,
            max_length=max_length,
            min_length=min_length,
            do_sample=False,
            truncation=True
        )

        summaries.append(result[0]["summary_text"])

    return " ".join(summaries)
