import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("", True),
        ("a", True),
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("Alphabet", False),
        ("Dermatoglyphics", True),
        ("isogram", True),
        ("hello", False),
        ("Aa", False),
    ],
)
def test_is_isogram(word: str, expected: str) -> None:
    assert is_isogram(word) is expected
