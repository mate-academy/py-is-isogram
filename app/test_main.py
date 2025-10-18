import pytest
from app.main import is_isogram


def test_empty_string_is_isogram() -> None:
    """Test that empty string is considered an isogram."""
    assert is_isogram("") is True


def test_unique_letters_lowercase() -> None:
    """Test lowercase word with unique letters returns True."""
    assert is_isogram("playgrounds") is True


def test_repeated_letters_consecutive() -> None:
    """Test word with consecutive repeated letters returns False."""
    assert is_isogram("look") is False


def test_repeated_letters_non_consecutive() -> None:
    """Test word with non-consecutive repeating letters returns False."""
    assert is_isogram("banana") is False


def test_case_insensitive_check() -> None:
    """Test that letter case is ignored during check."""
    assert is_isogram("Adam") is False
    assert is_isogram("Isogram") is True


@pytest.mark.parametrize(
    "word, expected",
    [
        ("", True),
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("isogram", True),
        ("Letter", False),
        ("Machine", True),
    ],
)
def test_parametrized_is_isogram(word: str, expected: bool) -> None:
    """Test multiple words for isogram property using parameterization."""
    assert is_isogram(word) is expected
