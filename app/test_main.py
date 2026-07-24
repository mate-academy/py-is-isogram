import pytest

from app.main import is_isogram


@pytest.mark.parametrize("word", [
    "playgrounds",
    "Dermatoglyphics",
    "",
])
def test_is_isogram_true(word: str) -> None:
    assert is_isogram(word) is True


@pytest.mark.parametrize("word", [
    "look",
    "Adam",
    "moOse",
])
def test_is_isogram_false(word: str) -> None:
    assert is_isogram(word) is False
