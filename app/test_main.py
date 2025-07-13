from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word, expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
    ],
    ids=[
        "all_unique_letters",
        "repeated_letters_look",
        "case_insensitive_false",
        "empty_string",
    ]
)
def test_is_isogram(word: str, expected: str) -> None:
    assert is_isogram(word) == expected
