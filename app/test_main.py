from app.main import is_isogram
import pytest


class TestIsIsogram:
    """Test cases for the is_isogram function."""

    # Basic positive cases - valid isograms
    def test_simple_isogram(self) -> None:
        """Test a simple word with no repeating letters."""
        assert is_isogram("playgrounds") is True

    def test_single_letter(self) -> None:
        """Test a single letter word is an isogram."""
        assert is_isogram("a") is True

    def test_two_different_letters(self) -> None:
        """Test a word with two different letters."""
        assert is_isogram("ab") is True

    def test_isogram_with_various_letters(self) -> None:
        """Test various isograms."""
        assert is_isogram("background") is True
        assert is_isogram("downstream") is True
        assert is_isogram("abcdefghijklmnopqrstuvwxyz") is True

    # Basic negative cases - words with repeating letters
    def test_consecutive_repeating_letters(self) -> None:
        """Test word with consecutive repeating letters."""
        assert is_isogram("look") is False

    def test_non_consecutive_repeating_letters(self) -> None:
        """Test word with non-consecutive repeating letters."""
        assert is_isogram("eleven") is False
        assert is_isogram("alphabet") is False

    def test_multiple_repeating_letters(self) -> None:
        """Test word with multiple letters repeated."""
        assert is_isogram("mississippi") is False

    # Case insensitivity tests
    def test_case_insensitive_same_letter_uppercase(self) -> None:
        """Test that uppercase and lowercase are equal."""
        assert is_isogram("Adam") is False

    def test_case_insensitive_mixed_case(self) -> None:
        """Test mixed case with repeating letters."""
        assert is_isogram("Alphabet") is False
        assert is_isogram("AbC") is True

    def test_all_uppercase_isogram(self) -> None:
        """Test all uppercase isogram."""
        assert is_isogram("BACKGROUND") is True

    def test_all_uppercase_non_isogram(self) -> None:
        """Test all uppercase non-isogram."""
        assert is_isogram("LOOK") is False

    def test_mixed_case_isogram(self) -> None:
        """Test mixed case isogram."""
        assert is_isogram("AbCdEfG") is True

    def test_first_last_same_letter_different_case(self) -> None:
        """Test word with same letter in different case."""
        assert is_isogram("Anna") is False

    # Edge cases
    def test_empty_string(self) -> None:
        """Test that empty string is considered an isogram."""
        assert is_isogram("") is True

    def test_repeated_letter_at_start(self) -> None:
        """Test word with repeated letter at the start."""
        assert is_isogram("aardvark") is False

    def test_repeated_letter_at_end(self) -> None:
        """Test word with repeated letter at the end."""
        assert is_isogram("kayak") is False

    def test_long_isogram(self) -> None:
        """Test a longer isogram."""
        assert is_isogram("uncopyrightable") is True

    def test_long_non_isogram(self) -> None:
        """Test a longer non-isogram."""
        assert is_isogram("programming") is False


# Additional parametrized tests for better coverage
class TestIsIsogramParametrized:
    """Parametrized tests for better test coverage."""

    @pytest.mark.parametrize("word", [
        "playgrounds",
        "background",
        "downstream",
        "a",
        "ab",
        "AbC",
        "BACKGROUND",
        "uncopyrightable",
        "",
    ])
    def test_valid_isograms(self, word: str) -> None:
        """Test various valid isograms."""
        assert is_isogram(word) is True

    @pytest.mark.parametrize("word", [
        "look",
        "Adam",
        "eleven",
        "alphabet",
        "mississippi",
        "Alphabet",
        "LOOK",
        "Anna",
        "aardvark",
        "kayak",
    ])
    def test_invalid_isograms(self, word: str) -> None:
        """Test various non-isograms."""
        assert is_isogram(word) is False

    @pytest.mark.parametrize("word,expected", [
        ("A", True),
        ("AA", False),
        ("Aa", False),
        ("aA", False),
        ("abc", True),
        ("aBc", True),
        ("abC", True),
        ("ABC", True),
        ("aba", False),
        ("AbA", False),
    ])
    def test_case_variations(self, word: str, expected: bool) -> None:
        """Test various case combinations."""
        assert is_isogram(word) is expected
