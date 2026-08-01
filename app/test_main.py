from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word, expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("Isogram", True),
        ("aba", False),
    ],
    ids=[
        "unique_letters",
        "duplicate_consecutive",
        "case_insensitive_duplicate",
        "empty_string",
        "long_isogram",
        "duplicate_non_consecutive",
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) is expected
