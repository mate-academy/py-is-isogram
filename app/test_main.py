from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word,words_boolean",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True)
    ],
    ids=(
        "word 'playground' check",
        "word 'look' check",
        "name 'Adam' check",
        "empty string check"
    )
)
def test_if_the_word_is_isogram(
        word: str,
        words_boolean: bool
) -> None:
    assert is_isogram(word) == words_boolean


@pytest.mark.parametrize(
    "word",
    [1]
)
def test_error(word: int) -> None:
    with pytest.raises(AttributeError):
        is_isogram(word)
