import pytest

from app import main


@pytest.mark.parametrize(
    "word, expected",
    [
        ("", True),
        ("a", True),
        ("playgrounds", True),
        ("machine", True),
        ("look", False),
        ("Adam", False),
        ("aba", False),
        ("Alphabet", False),
        ("HELlo", False),
    ],
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert main.is_isogram(word) is expected
