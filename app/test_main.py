import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    ("word", "expected"),
    [
        ("Mark", True),
        ("playground", True),
        ("look", False),
        ("", True),
        ("phone", True)
    ],
    ids = [
        "all_unique_lowercase",
        "repeated_letters",
        "case_insensitive",
        "empty_string",
        "mixed_case",
    ]
)
def test_for_words(
    word: str,
    expected: bool
) -> None:
    assert is_isogram(word) == expected
