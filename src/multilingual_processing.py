from transformers import pipeline

# Translate article to target language
def translate_article(article_text, target_language="en"):
    try:
        translator = pipeline("translation", model=f"Helsinki-NLP/opus-mt-{target_language}-en")
        translated = translator(article_text, max_length=512)[0]["translation_text"]
        return translated
    except Exception as e:
        return f"Translation error: {str(e)}"
