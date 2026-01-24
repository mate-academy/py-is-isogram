import pytest
from app import main


@pytest.mark.parametrize(
    "word,expected",
    [
        ("", True),
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("isogram", True),
        ("aba", False),
        ("Alphabet", False),
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert main.is_isogram(word) is expected
