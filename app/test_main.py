from app.main import is_isogram
import pytest


@pytest.mark.parametrize("word, result",
                         [
                             ("", True),
                             ("playgrounds", True),
                             ("look", False),
                             ("Adam", False),
                             ("Isogram", True),
                             ("asdfghjklQWERT", True)
                         ])
def test_is_isogram(word: str, result: bool) -> None:
    assert is_isogram(word) == result
