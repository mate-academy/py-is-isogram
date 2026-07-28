import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected",
    [
        ("", True),
        ("a", True),
        ("playgrounds", True),
        ("Dermatoglyphics", True),
        ("look", False),
        ("Adam", False),
        ("aba", False),
        ("Alphabet", False),
    ],
    ids=[
        "empty string",
        "single letter",
        "lowercase isogram",
        "mixed case isogram",
        "duplicate lowercase letters",
        "case insensitive duplicate",
        "non consecutive duplicate",
        "mixed case duplicate",
    ],
)
def test_is_isogram(
    word: str,
    expected: bool,
) -> None:
    assert is_isogram(word) is expected
