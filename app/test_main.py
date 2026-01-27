from app.main import is_isogram
import pytest


@pytest.mark.parametrize("word,expected",
                         [("playgrounds", True),
                          ("Adam", False),
                          ("Alex", True),
                          ("", True),
                          ("look", False)])
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
