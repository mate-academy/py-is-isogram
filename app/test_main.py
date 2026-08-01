from app.main import is_isogram

import pytest


@pytest.mark.parametrize(
    "word,expected",
    [
        ("playground", True),
        ("look", False),
        ("Adam", False),
        ("", True)
    ],
    ids=[
        "playground should return True",
        "look should return False",
        "Adam should return False (checking case sensitivity)",
        "Empty string should return True",
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
