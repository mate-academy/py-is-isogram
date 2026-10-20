import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("", True),
        ("a", True),
        ("playgrounds", True),
        ("Dermatoglyphics", True),
        ("look", False),
        ("Adam", False),
        ("moose", False),
        ("aba", False),
        ("aA", False),
    ],
    ids=[
        "empty_string",
        "single_letter",
        "valid_isogram",
        "valid_isogram_mixed_case",
        "consecutive_repeats",
        "case_insensitive_repeat",
        "multiple_repeats",
        "sandwich_repeat",
        "same_letter_different_case",
    ],
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected


def test_is_isogram_returns_bool() -> None:
    result = is_isogram("test")
    assert isinstance(result, bool)
