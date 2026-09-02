import pytest

from app import main


@pytest.mark.parametrize(
    "word, expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("a", True),
        ("aa", False),
        ("AaBb", False),
        ("dermatoglyphics", True),
        ("moOse", False),
        ("isogram", True),
    ],
    ids=[
        "no_repeated_letters",
        "consecutive_repeated_letters",
        "non_consecutive_repeated_letters_case_insensitive",
        "empty_string",
        "single_letter",
        "two_identical_letters",
        "mixed_case_repeated_letter",
        "long_word_no_repeats",
        "case_insensitive_repeat_moOse",
        "word_isogram_itself",
    ],
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert main.is_isogram(word) is expected
