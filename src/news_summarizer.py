from transformers import pipeline

# Generate news summary using Llama (simulated with OPT-350m)
def summarize_news(article_text, language="en"):
    generator = pipeline("text-generation", model="facebook/opt-350m")  # Llama placeholder
    prompt = f"Summarize this news article in {language}: {article_text}"
    summary = generator(prompt, max_length=100, num_return_sequences=1)[0]["generated_text"]
    return summary
