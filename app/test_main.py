import pytest

from app import main


@pytest.mark.parametrize(
    "word,expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("a", True),
        ("ab", True),
        ("aa", False),
        ("Moon", False),
        ("background", True),
        ("isogram", True),
        ("subdermatoglyphic", True),
        ("Alphabet", False),
    ],
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert main.is_isogram(word) is expected
