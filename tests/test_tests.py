import pytest
from app.main import is_isogram


def test_isogram_is_case_insensitive():
    """Ensure case insensitivity in isogram checking."""
    assert is_isogram("Adam") == False
    assert is_isogram("Dermatoglyphics") == True


def test_empty_string_is_isogram():
    """An empty string should be an isogram."""
    assert is_isogram("") == True


def test_non_consecutive_letters_are_not_isogram():
    """A word with non-consecutive duplicate letters is not an isogram."""
    assert is_isogram("banana") == False
    assert is_isogram("look") == False


def test_consecutive_letters_are_not_isogram():
    """A word with consecutive duplicate letters is not an isogram."""
    assert is_isogram("letter") == False
    assert is_isogram("hello") == False


def test_valid_isograms():
    """Valid isograms should return True."""
    assert is_isogram("playgrounds") == True
    assert is_isogram("subdermatoglyphic") == True
    assert is_isogram("isogram") == True


def test_single_letter_is_isogram():
    """A single letter is always an isogram."""
    assert is_isogram("a") == True
    assert is_isogram("Z") == True
