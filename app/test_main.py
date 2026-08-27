import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("", True),
        ("a", True),
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("isogram", True),
        ("Alphabet", False),
        ("moOse", False),
    ],
    ids=[
        "empty_string",
        "single_character",
        "valid_isogram_lowercase",
        "consecutive_repeating_letters",
        "case_insensitive_repeating_first_and_last",
        "unique_letters_lowercase",
        "case_insensitive_repeating_first_and_middle",
        "case_insensitive_consecutive_repeating",
    ],
)
def test_is_isogram(word, expected):
    assert is_isogram(word) is expected
