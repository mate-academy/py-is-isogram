import pytest
from app.main import is_isogram


@pytest.mark.parametrize("word, expected",
                         [("playgrounds", True),
                          ("look", False),
                          ("Adam", False),
                          ("", True),
                          ])
def test_is_isogram_with_different_words(word: str, expected: bool) -> None:
    assert expected == is_isogram(word)
