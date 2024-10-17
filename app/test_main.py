import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",  # Correctly group parameters together
    [
        ("playgrounds", True),  # no repeating letters
        ("look", False),        # repeating 'o'
        ("Adam", False),        # 'A' and 'a' are the same
        ("", True),             # empty string is an isogram
        ("qwertyuio", True),    # all unique letters
        ("A", True),            # single letter is an isogram
        ("Aa", True),           # upper and lowercase letter
        ("mate", True),         # no repeating letters
    ],
    ids=[
        "no_repeating_letters",
        "repeating_o",
        "case_insensitive_A",
        "empty_string",
        "all_unique_letters",
        "single_letter",
        "same_letter_different_cases",
        "no_repeating_in_mate",
    ],
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
