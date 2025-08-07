from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word, expected",
    [
        ("python", True),
        ("playground", True),
        ("look", False),
        ("Adam", False),
        ("Nowhere", False),
        ("crazy", True),
        ("", True)
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    result = is_isogram(word)
    assert result == expected, f"Expected {expected}, got {result}"
