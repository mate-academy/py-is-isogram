import pytest

from app.main import is_isogram


def test_empty_string_is_isogram():
    assert is_isogram("") is True


def test_single_letter_is_isogram():
    assert is_isogram("a") is True


def test_simple_isogram():
    assert is_isogram("playgrounds") is True


def test_repeating_letters_not_isogram():
    assert is_isogram("look") is False


def test_case_insensitive_check():
    assert is_isogram("Adam") is False


def test_all_unique_uppercase():
    assert is_isogram("DERMATOGlyphics".upper()) is True


def test_mixed_case_unique_letters():
    assert is_isogram("Dermatoglyphics") is True


def test_multiple_repeated_letters():
    assert is_isogram("mississippi") is False


def test_long_isogram():
    assert is_isogram("subdermatoglyphic") is True


def test_repeated_non_consecutive_letters():
    assert is_isogram("alphabet") is False
