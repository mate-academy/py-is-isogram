from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word,boolean",
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
        boolean: bool
) -> None:
    assert is_isogram(word) == boolean
