import pytest


@pytest.mark.parametrize("word, expected", [
    ("", True),
    ("z", True),
    ("playgrounds", True),
    ("look", False),
    ("alphabet", False),
    ("Adam", False),
    ("Aa", False),
])
def is_isogram(word: str) -> bool:
    word_lower = word.lower()
    return len(set(word_lower)) == len(word_lower)
