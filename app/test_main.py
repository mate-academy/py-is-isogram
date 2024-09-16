from app.main import is_isogram

import pytest


@pytest.mark.parametrize(
    "word,expected_result",
    [
        pytest.param("playgrounds", True, id="word is isogram"),
        pytest.param("look", False, id="word is not isogram"),
        pytest.param("Adam", False, id="capitalized word is isogram"),
        pytest.param("Jon", True, id="capitalized word is not isogram"),
        pytest.param("", True, id="empty string")
    ]
)
def test_word_is_isogram(word, expected_result):
    assert is_isogram(word) == expected_result
