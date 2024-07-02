import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, is_word_isogram",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
    ]
)
def test_is_the_word_check_correct(word: str, is_word_isogram: bool) -> None:
    assert is_isogram(word) == is_word_isogram
