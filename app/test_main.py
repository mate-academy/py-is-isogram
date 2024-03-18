import pytest

from app.main import is_isogram


@pytest.mark.parametrize("word, expected_result", [
    ("", True),
    ("playgrounds", True),
    ("look", False),
    ("Adam", False),
])
def test_is_isogram(word: str, expected_result: bool) -> None:
    assert is_isogram(word) == expected_result
