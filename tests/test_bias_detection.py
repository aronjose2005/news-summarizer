import pytest
from src.bias_detection import detect_bias

def test_detect_bias():
    article = "This policy is the best ever!"
    result = detect_bias(article)
    assert "bias_label" in result
    assert "bias_score" in result
    assert 0 <= result["bias_score"] <= 1
