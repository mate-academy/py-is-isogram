from app.main import is_isogram

import pytest


@pytest.mark.parametrize(
    "word,expected",
    [
        pytest.param(
            "", True,
            id="should return `True` if word is empty string"
        ),
        pytest.param(
            "a", True,
            id="should return `True` if `word` contains 1 letter"
        ),
        pytest.param(
            "Adam", False,
            id="should return `False` as func is case-insensitive"
        ),
        pytest.param(
            "look", False,
            id="should return `False` if word has repeating letters"
        ),
    ]
)
def test_is_isogram(word: str, expected: str):
    assert is_isogram(word) == expected
