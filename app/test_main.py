from typing import Any
import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word",
    [
        "playgrounds",
        "",
        "subdermatoglyphic",
    ],
)
def test_is_isogram_true_cases(word: str) -> None:
    assert is_isogram(word) is True


@pytest.mark.parametrize(
    "word",
    [
        "look",
        "Adam",
        "Alphabet",
    ],
)
def test_is_isogram_false_cases(word: str) -> None:
    assert is_isogram(word) is False


@pytest.mark.parametrize(
    "wrong_word",
    [
        123,
        15.5,
        None,
        True,
        False,
        ["a", "b"],
    ],
)
def test_is_isogram_invalid_types(wrong_word: Any) -> None:
    with pytest.raises(TypeError):
        is_isogram(wrong_word)
