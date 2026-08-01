import pytest
from app.main import is_isogram
from typing import Any


@pytest.mark.parametrize(
    "word,expected",
    [
        ("", True),
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("Alphabet", False),
        ("six-year-old", True),
    ]
)
def test_is_isogram_values(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected


@pytest.mark.parametrize(
    "word",
    [
        123,
        None,
        ["word"],
        10.5,
    ]
)
def test_is_isogram_raises_type_error(word: Any) -> None:
    with pytest.raises(TypeError):
        is_isogram(word)
