from app.main import is_isogram

import pytest


@pytest.mark.parametrize("word, expected", [
    ("playgrounds", True),
    ("look", False),
    ("Adam", False),
    ("", True),
    ("hello", False),
    ("algorithm", True)
])
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
