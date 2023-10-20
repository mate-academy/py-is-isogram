from app.main import is_isogram

import pytest


@pytest.mark.parametrize(
    "word, expected",
    [
        ("look", False),
        ("Adam", False),
        ("", True,)
    ],
    ids=[
        "Word mustn't have repeating letters",
        "Function should be case-insensitive",
        "Empty string is `Isogram`"
    ]
)
def test_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
