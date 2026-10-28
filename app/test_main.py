import pytest
from app import main


@pytest.mark.parametrize(
    "word, expected",
    [
        ("", True),
        ("playgrounds", True),
        ("subdermatoglyphic", True),
        ("Adam", False),
        ("Alphabet", False),
        ("aA", False),
        ("look", False),
        ("letter", False),
        ("eleven", False),
        ("mama", False),
    ],
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert main.is_isogram(word) is expected
