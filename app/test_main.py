import pytest

from app.main import is_isogram


# write your code here
@pytest.mark.parametrize("word, expected_result", [
    ("", True),
    ("look", False),
    ("Adam", False),
    ("playgrounds", True),
])
def test_whether_is_isogram(word: str, expected_result: bool) -> None:
    assert is_isogram(word) == expected_result
