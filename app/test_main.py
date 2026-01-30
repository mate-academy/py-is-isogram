import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("", True),
        ("play", True),
        ("subdermatoglyphic", True),
        ("moo", False),
        ("look", False),
        ("aba", False),
        ("Adam", False),
        ("Aa", False),
        ("Alphabet", False),
        ("éléphant", False),
        ("nn", False),
    ]
)
def test_is_isogram_various_cases(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
