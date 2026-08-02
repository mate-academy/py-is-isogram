import pytest
from typing import Any
from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected",
    [
        ("", True),
        ("a", True),
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected


@pytest.mark.parametrize(
    "word,expected_error",
    [
        (1, TypeError),
        ([], TypeError),
        ({}, TypeError),
    ]
)
def test_is_empty_string(
        word: type[Any],
        expected_error: type[Exception]
) -> None:
    with pytest.raises(expected_error):
        is_isogram(word)
