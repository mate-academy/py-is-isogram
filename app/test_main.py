import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected",
    [
        ("", True),
        ("aAa", False),
        ("Python", True),
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
    ]
)
def test_word_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
