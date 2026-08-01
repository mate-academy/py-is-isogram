from app.main import is_isogram
import pytest


@pytest.mark.parametrize("word, expected", [
    ("playgrounds", True),
    ("Artem", True),
    ("look", False),
    ("Madagascar", False),
    ("", True),
    ("Adam", False),
    ("Python", True),
])
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
