from app.main import is_isogram
import pytest


@pytest.mark.parametrize("word, new_word", [
    ("abcd", True),
    ("look at me", False),
    ("none", False),
    ("father", True),
    ("", True),
    ("am ns", True),
    ("Mom", False)
])
def test_should_check_if_the_letter_is_repeated(
        word: str, new_word: list
) -> bool:
    worder = is_isogram(word)
    assert worder == new_word
