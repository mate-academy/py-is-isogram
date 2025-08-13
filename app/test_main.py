from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word, expected",
    [
    ("playground", True),
    ("look", False),
    ("Adam", False),
    ("", True)
    ]
)

def test_if_words_lower(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
