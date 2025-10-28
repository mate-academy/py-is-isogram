import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected",
    [
        ("", True),
        ("a", True),
        ("Aa", False),
        ("look", False),
        ("Adam", False),
        ("playgrounds", True),
        ("STAR", True)
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
