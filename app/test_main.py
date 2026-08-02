from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word, expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("aA", False),
        ("abcdefg", True),
        ("letter", False),
    ],
)
def test_is_isogram(word: str, expected: str) -> None:
    assert is_isogram(word) is expected
