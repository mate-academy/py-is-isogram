from typing import Any
import pytest
from app import main


@pytest.mark.parametrize(
    "word, expected",
    [
        ("", True),
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("Hello", False),
        ("World", True),
        ("aba", False),
        ("abcabc", False),
        ("aa", False),
        ("book", False),
        ("Django", True),
        ("Cat", True),
    ],
)
def test_is_isogram_valid_cases(word: str, expected: bool) -> None:
    assert main.is_isogram(word) == expected


@pytest.mark.parametrize(
    "invalid_input",
    [
        123,
        10.5,
        None,
        ["word"],
        {"word": True},
    ],
)
def test_is_isogram_invalid_types(invalid_input: Any) -> None:
    with pytest.raises(TypeError):
        main.is_isogram(invalid_input)
