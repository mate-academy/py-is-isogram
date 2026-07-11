from typing import Any
import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        "playgrounds", True,
        "", True,
        "", True,
        "look", False,
        "Adam", False,
        "Alphabet", False,
    ],
)
def test_is_isogram_valid_cases(word: str, expected: bool) -> None:
    assert is_isogram(word) is expected


@pytest.mark.parametrize(
    "wrong_word",
    [
        123,
        15.5,
        None,
        True,
        False,
        (["a", "b"]),
    ],
)
def test_is_isogram_invalid_types(wrong_word: Any) -> None:
    with pytest.raises(TypeError):
        is_isogram(wrong_word)
