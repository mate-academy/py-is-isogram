from typing import Any
import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected",
    [
        ("", True),
        ("a", True),
        ("subdermatoglyphic", True),
        ("QuIz", True),
        ("Adam", False),
        ("pipe", False),
        ("Alphabet", False),
        ("LoOk", False),
        ("playGrounds", True),
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    result = is_isogram(word)
    assert result == expected


@pytest.mark.parametrize(
    "invalid_input",
    [1234, 2.5, None, ["a", "b"], {"word": "abd"}, True]
)
def test_is_isogram_invalid_input(invalid_input: Any) -> None:
    with pytest.raises((TypeError, ValueError)):
        is_isogram(invalid_input)


def test_is_isogram_returns_isogram_only() -> None:
    words = ["subdermatoglyphic",
             "quiz",
             "playgrounds",
             "look",
             "",
             "Adam",
             "quiz"
             ]
    for word in words:
        result = is_isogram(word)
        assert isinstance(result, bool)
