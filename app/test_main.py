from app.main import is_isogram
import pytest


def test_empty_str():
    assert is_isogram("") == True


def test_isogram_single_character():
    assert is_isogram('a') == True


def test_isogram_playgrounds():
    assert is_isogram('playgrounds') == True


def test_isogram_look():
    assert is_isogram('look') == False


def test_isogram_Adam():
    assert is_isogram('Adam') == False


def test_isogram_uppercase_mixed():
    assert is_isogram('Alphabet') == False


def test_isogram_case_insensitive():
    assert is_isogram('Dermatoglyphics') == True


def test_isogram_long_non_isogram():
    assert is_isogram('subdermatoglyphic') == True


def test_isogram_with_repeated_characters():
    assert is_isogram('eleven') == False


def test_isogram_with_unique_characters():
    assert is_isogram('subway') == True


def test_isogram_with_all_alphabets():
    assert is_isogram('abcdefghijklmnopqrstuvwxyz') == True
