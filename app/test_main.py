from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word,expected",
    [
        ("word", True),
        ("revers", False),
        ("Litle", False),
        ("", True),
        ("banana", False),
        ("alphabet", False),
        ("moOse", False),
        ("aba", False)
    ]
)
def test_is_isogram(word: str, expected: str) -> None:
    assert is_isogram(word) == expected
