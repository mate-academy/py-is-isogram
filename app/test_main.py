from app.main import is_isogram
import pytest


@pytest.mark.parametrize("word, expected", [
    ("playgrounds", True),
    ("look", False),
    ("Adam", False),
    ("", True),
    ("isogram", True),
    ("Consecutive", False),
])
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected, \
        (f"Expected '{word}' to be "
         f"{'an isogram' if expected else 'not an isogram'}")
