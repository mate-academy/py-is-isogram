import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("", True),
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("isogram", True),
        ("Alphabet", False),
        ("A", True),
        ("aa", False),
    ],
    ids=[
        "empty_string",
        "valid_lowercase_isogram",
        "consecutive_repeats",
        "case_insensitive_repeats",
        "valid_longer_isogram",
        "non_consecutive_case_insensitive",
        "single_letter",
        "smallest_non_isogram"
    ]
)
def test_is_isogram_standard_cases(word: str, expected: bool) -> None:
    result = is_isogram(word)
    assert result is expected
    assert isinstance(result, bool)
