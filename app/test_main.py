from app.main import is_isogram
import pytest


@pytest.mark.parametrize("word, value", [
    ("playgrounds", True),
    ("look", False),
    ("Adam", False),
    ("", True),

])
def test_is_isogram(word: str, value: bool) -> None:
    assert is_isogram(word) == value
