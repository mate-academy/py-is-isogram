from pickle import FALSE
from app.main import is_isogram
import pytest


@pytest.mark.parametrize("word, definition", [
    ("playgrounds", True),
    ("look", FALSE),
    ("Adam", FALSE),
    (" ", True)
])
def test_word_iso(word: str, definition: bool) -> None:
    result = is_isogram(word)
    result == definition

# write your code here
