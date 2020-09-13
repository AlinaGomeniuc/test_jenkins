import pytest
from app import analyze_word, input_word

def test_analyze_word_false():
    word = "time"
    res = analyze_word(word, [])
    assert len(res) == len(word) * 2


def test_analyze_word_true():
    word = "time"
    res = analyze_word(word, ["t", "i", "m", "e"])
    assert "-" not in res


def test_input_word():
    word = "time"
    bool = input_word(word)
    assert bool == True


def test_input_word_error():
    word = ""
    with pytest.raises(Exception):
        input_word(word)
