import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word",
    [
        ("playgrounds"),
        ("a"),
        ("")
    ]
)
def test_isogram_with_isogram_word(word: str) -> None:
    assert is_isogram(word)

@pytest.mark.parametrize(
    "word",
    [
        ("look"),
        ("Adam"),
    ]
)
def test_isogram_with_not_isogram_word(word: str) -> None:
    assert not is_isogram(word)