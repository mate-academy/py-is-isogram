import pytest
from app.main import is_isogram


class TestIsIsogram:
    """Test class for is_isogram function."""

    def test_empty_string_is_isogram(self) -> None:
        """Test that empty string is considered an isogram."""
        assert is_isogram("") is True

    @pytest.mark.parametrize("word", ["a", "A", "z", "B", "x"])
    def test_single_character_is_isogram(self, word: str) -> None:
        """Test that single character strings are isograms."""
        assert is_isogram(word) is True

    @pytest.mark.parametrize(
        "word",
        [
            "playgrounds",
            "background",
            "abcdef",
            "uncopyrightable",
            "ABCD",
            "subdermatoglyphic",
            "uncopyrightables",
        ],
    )
    def test_valid_isograms(self, word: str) -> None:
        """Test strings that are valid isograms (no repeating letters)."""
        assert is_isogram(word) is True

    @pytest.mark.parametrize(
        "word", ["look", "book", "eleven", "aabbcc", "hello", "troubleshooting"]
    )
    def test_invalid_isograms_with_repeating_letters(self, word: str) -> None:
        """Test strings that are not isograms due to repeating letters."""
        assert is_isogram(word) is False

    @pytest.mark.parametrize(
        "word,expected",
        [
            ("Adam", False),
            ("Aa", False),
            ("aA", False),
            ("AbC", True),
            ("AbA", False),
            ("MoM", False),
            ("Mom", False),
            ("Background", True),
            ("AbCdEf", True),
            ("Playground", True),
        ],
    )
    def test_case_insensitive_and_mixed_case(
        self, word: str, expected: bool
    ) -> None:
        """Test case-insensitive behavior and mixed case scenarios."""
        assert is_isogram(word) is expected

    @pytest.mark.parametrize("word", ["Letter", "Balloon", "Coffee"])
    def test_mixed_case_invalid_isograms(self, word: str) -> None:
        """Test mixed case strings that are invalid isograms."""
        assert is_isogram(word) is False

    @pytest.mark.parametrize("word", ["aa", "aaa", "AAAA", "bbbb"])
    def test_all_same_letters(self, word: str) -> None:
        """Test strings with all same letters."""
        assert is_isogram(word) is False


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("", True),
        ("isogram", True),
        ("eleven", False),
        ("Isogram", True),
        ("IsOgRaM", True),
        ("LOOK", False),
    ],
)
def test_comprehensive_isogram_cases(test_input: str, expected: bool) -> None:
    """Comprehensive test cases covering all main scenarios."""
    assert is_isogram(test_input) is expected
