from app.main import is_isogram

import pytest


@pytest.mark.parametrize(
    "input_word,expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("", True),
        ("Adam", False)
    ]
)
def test_is_isogram(input_word: str, expected: bool) -> None:
    assert is_isogram(input_word) == expected
