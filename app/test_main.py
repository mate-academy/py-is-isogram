from app import main
import pytest


@pytest.mark.parametrize(
    "word, expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("Aa", False),
        ("aba", False),
        ("abc", True)
    ]
)
def test_isograms(word: str, expected: bool) -> None:
    assert main.is_isogram(word) == expected
