import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ('playgrounds', True),  # No repeating letters
        ('look', False),        # 'o' repeats
        ('Adam', False),        # 'A' and 'a' are the same letter, case-insensitive
        ('', True),             # Empty string is considered an isogram
        ('abcde', True),        # No repeating letters, all unique
        ('aabbcc', False),      # Letters repeat
        ('Unique', False),      # 'U' and 'u' are the same letter
        ('Isogram', True),      # No repeating letters
        ('Alphabet', False),   # 'a' repeats
    ]
)
def test_is_isogram(word, expected):
    assert is_isogram(word) == expected
