import pytest
from app import main


def test_isogram_is_case_insensitive():
    """Test that function is case-insensitive."""
    assert main.is_isogram("Adam") == False, "String with different cases of the same letter is not an isogram."


def test_empty_string_is_isogram():
    """Test that empty string is considered an isogram."""
    assert main.is_isogram("") == True, "Empty string should be an isogram."


def test_non_consecutive_letters_are_not_isogram():
    """Test that non-consecutive repeating letters make the word not an isogram."""
    assert main.is_isogram("banana") == False, "Non-consecutive repeating letters are not handled properly."


def test_consecutive_letters_are_not_isogram():
    """Test that consecutive repeating letters make the word not an isogram."""
    assert main.is_isogram("look") == False, "Consecutive repeating letters are not handled properly."