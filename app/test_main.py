from app.main import is_isogram

import pytest


@pytest.mark.parametrize(
    "word,expected",
    [
        ("12345", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("Andrey", True),
        ("f-!d", True),
        (" ", True)
    ],
    ids=[
        "test_returns_true_when_word_is_12345",
        "test_returns_false_when_word_is_look",
        "test_returns_false_when_word_is_Adam",
        "test_returns_true_when_word_is_empty",
        "test_returns_true_when_word_is_Andrey",
        "test_returns_true_when_word_is_f-!d",
        "test_returns_true_when_word_is_space",
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
