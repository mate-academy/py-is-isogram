import pytest
from app.main import is_isogram


class TestIsIsogram:
    """Test cases for is_isogram function."""

    def test_empty_string_is_isogram(self):
        """Test that empty string is considered an isogram."""
        assert is_isogram('') is True

    def test_single_letter_is_isogram(self):
        """Test that single letter is an isogram."""
        assert is_isogram('a') is True
        assert is_isogram('Z') is True

    def test_word_with_no_repeating_letters(self):
        """Test words with no repeating letters."""
        assert is_isogram('playgrounds') is True
        assert is_isogram('background') is True
        assert is_isogram('python') is True

    def test_word_with_repeating_letters(self):
        """Test words with repeating letters."""
        assert is_isogram('look') is False
        assert is_isogram('hello') is False
        assert is_isogram('programming') is False

    def test_case_insensitive(self):
        """Test that function is case-insensitive."""
        assert is_isogram('Adam') is False
        assert is_isogram('AbC') is True
        assert is_isogram('AaB') is False
        assert is_isogram('XyZ') is True

    def test_mixed_case_with_repeating_letters(self):
        """Test mixed case words with repeating letters."""
        assert is_isogram('Hello') is False
        assert is_isogram('WoRlD') is False
        assert is_isogram('AbCdEfG') is True

    def test_all_same_letters(self):
        """Test words with all same letters."""
        assert is_isogram('aaa') is False
        assert is_isogram('AAA') is False
        assert is_isogram('AaA') is False

    def test_alternating_case_same_letters(self):
        """Test alternating case of same letters."""
        assert is_isogram('AaBbCc') is False
        assert is_isogram('AbAb') is False

    def test_long_isogram(self):
        """Test longer words that are isograms."""
        assert is_isogram('uncopyrightable') is True
        assert is_isogram('dermatoglyphics') is True

    def test_long_non_isogram(self):
        """Test longer words that are not isograms."""
        assert is_isogram('subdermatoglyphic') is False
        assert is_isogram('incomprehensible') is False

    @pytest.mark.parametrize("word,expected", [
        ('', True),
        ('a', True),
        ('ab', True),
        ('abc', True),
        ('abcd', True),
        ('aa', False),
        ('aba', False),
        ('abca', False),
        ('AbC', True),
        ('AaB', False),
        ('playgrounds', True),
        ('look', False),
        ('Adam', False),
    ])
    def test_parametrized_cases(self, word, expected):
        """Parametrized test cases for various inputs."""
        assert is_isogram(word) is expected
