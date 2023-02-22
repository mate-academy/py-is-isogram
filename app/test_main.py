from app.main import is_isogram

import pytest


@pytest.mark.parametrize(
    "word, expected_result",
    [
        ("", True),  # Test with empty string
        ("isogram", True),  # Test with isogram word
        ("Alphabet", False),  # Test with non-isogram word
        ("mammoth", False),  # Test with non-isogram word
        ("abcdefg", True),  # Test with isogram word
        ("TacoCat", False),  # Test with non-isogram word (case-insensitive)
        ("The quick brown fox jumps", False),  # Test with non-isogram sentence
    ],
)
def test_is_isogram(word: str, expected_result: bool) -> None:
    assert is_isogram(word) == expected_result
