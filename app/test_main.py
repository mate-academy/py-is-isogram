import pytest
from app import main


@pytest.mark.parametrize(
    "word,expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("Dermatoglyphics", True),
        ("isogram", True),
        ("moose", False),
        ("aba", False),
        ("abc", True),
        ("", True),
        ("a", True),
        ("Aa", False),
    ],
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert main.is_isogram(word) is expected
