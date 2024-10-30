import pytest
from app.main import is_isogram


@pytest.mark.parametrize("word, expected_result", [
    ("playgrounds", True),
    ("look", False),
    ("Adam", False),
    ("", True),
    ("abcdefg", True),
    ("abcdea", False),
    ("AaBbCc", False),
])
def test_is_isogram(word: str, expected_result: bool) -> None:
    assert is_isogram(word) == expected_result, \
        (f"Expected {expected_result} for word={word}, "
         f"but got {is_isogram(word)}")
