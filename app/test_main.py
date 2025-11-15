import pytest
from typing import Any
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True)
    ],
)
def test_is_isogram_function(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected


@pytest.mark.parametrize(
    "word",
    [
        1,
        None,
        (-2)
    ],
)
def test_type_of_value(word: Any) -> None:
    with pytest.raises(TypeError):
        is_isogram(word)
