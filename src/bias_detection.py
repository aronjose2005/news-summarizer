from transformers import pipeline

# Detect bias in news article using NLP
def detect_bias(article_text):
    sentiment_analyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
    result = sentiment_analyzer(article_text)[0]
    # Simplified bias detection: high sentiment score may indicate bias
    bias_score = result["score"] if result["label"] in ["POSITIVE", "NEGATIVE"] else 0.5
    bias_label = "biased" if bias_score > 0.8 else "neutral"
    return {"bias_label": bias_label, "bias_score": bias_score}
