import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("abcde", True),
        ("aabbcc", False),
        ("Unique", False),
        ("Isogram", True),
        ("Alphabet", False),
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
