import pytest

from app.main import is_isogram


@pytest.mark.parametrize("word, expected_results", [
    ("playgrounds", True),
    ("look", False),
    ("Adam", False),
    ("", True)
])
def tests(word: str, expected_results: bool) -> None:
    assert is_isogram(word) == expected_results
