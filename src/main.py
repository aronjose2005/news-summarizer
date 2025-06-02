from news_summarizer import summarize_news
from bias_detection import detect_bias
from multilingual_processing import translate_article

def main():
    # Sample news article
    article_text = "Local government announces new policy to increase taxes for infrastructure development."
    print(f"Original Article: {article_text}")

    # Translate article (example: to Spanish and back to English)
    translated_to_spanish = translate_article(article_text, target_language="es")
    print(f"Translated to Spanish: {translated_to_spanish}")
    translated_back = translate_article(translated_to_spanish, target_language="en")
    print(f"Translated back to English: {translated_back}")

    # Detect bias
    bias_result = detect_bias(article_text)
    print(f"Bias Detection: {bias_result}")

    # Generate summary
    summary = summarize_news(article_text, language="en")
    print(f"News Summary: {summary}")

if __name__ == "__main__":
    main()
