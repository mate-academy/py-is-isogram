import pytest
from app.main import is_isogram


@pytest.mark.parametrize("word, expected_result", [
    ("playgrounds", True),
    ("look", False),
    ("Adam", False),
    ("", True),
    ("ABcDeF", True),
    ("AaBb", False),
])
def test_that_word_is_isogram(word: str, expected_result: bool) -> None:
    assert is_isogram(word) == expected_result
