import pytest
from src.news_summarizer import summarize_news

def test_summarize_news():
    article = "Government announces new tax policy."
    summary = summarize_news(article, language="en")
    assert isinstance(summary, str)
    assert len(summary) > 0
