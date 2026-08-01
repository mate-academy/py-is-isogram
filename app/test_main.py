from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word,expected",
    [
        ("hello", False),
        ("Kid", True),
        ("Beatles", False),
        ("Elephant", False),
        ("", True),
    ],
)
def test_for_isogram(word: str, expected: bool) -> None:
    result = is_isogram(word)
    assert result == expected
