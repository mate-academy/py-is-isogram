from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word, expected", [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("isogram", True),
        ("hello", False),
        ("Python", True),
        ("Alphabet", False),
        ("Dermatoglyphics", True),
        ("aA", False)
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert (
        is_isogram(word) == expected
    ), f"Expected {expected} for word '{word}'"
