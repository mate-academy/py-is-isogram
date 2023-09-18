import pytest
from app.main import is_isogram


@pytest.mark.parametrize("word, expected_result", [
    ("MAKSI", True),
    ("", True),
    ("Maksim", False),
])
def test_check_different_cases_word_is_isogram(
        word: str,
        expected_result: bool
) -> None:
    assert is_isogram(word) == expected_result
