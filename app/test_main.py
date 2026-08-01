from __future__ import annotations
import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("", True),
        ("d", True),
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
    ],
)
def test_is_isogram_valid(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected


@pytest.mark.parametrize(
    "word",
    [
        "play grounds",      # contains space
        "play123",           # contains digits
        "play-grounds",      # contains hyphen
        "play!grounds",      # contains punctuation
    ],
)
def test_is_isogram_invalid_input(word: str) -> None:
    with pytest.raises(ValueError):
        is_isogram(word)


@pytest.mark.parametrize(
    "word",
    [
        123,
        3.14,
        None,
        ["playgrounds"],
    ],
)
def test_is_isogram_wrong_type(word: str) -> None:
    with pytest.raises(TypeError):
        is_isogram(word)
