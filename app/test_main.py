import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("", True),
        ("Isogram", True),
        ("hello", False),
        ("world", True),
        ("Python", True),
        ("Programming", False),
        ("abcdefg", True),
        ("aa", False),
        ("Cc", False),
        ("Hawai", False)
    ],
    ids=[
        "empty_string",
        "case_insensitivity_isogram",
        "repeated_l_in_hello",
        "no_repeats_in_world",
        "no_repeats_in_python",
        "repeated_g_and_r_in_programming",
        "all_unique_in_abcdefg",
        "two_identical_letters",
        "same_letters_diff_case",
        "non_consecutive_letters"
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
