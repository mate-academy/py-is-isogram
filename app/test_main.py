import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,word_is_isogram",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True)
    ]
)
def test_should_return_the_word_the_word_is_isogram(
    word: str,
    word_is_isogram: bool
) -> None:
    result = is_isogram(word)
    assert result == word_is_isogram
