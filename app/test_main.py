import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word",
    ["Dermatoglyphics", "isoDram", "", " ", "lisT"]
)
def test_is_isogram(word: str) -> None:
    assert is_isogram(word)


@pytest.mark.parametrize("word", ["aba", "moOse"])
def test_not_isogram(word: str) -> None:
    assert not is_isogram(word)
