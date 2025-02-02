import pytest
from app.main import is_isogram

def test_empty_string():
    assert is_isogram("") is True

def test_unique_letters():
    assert is_isogram("playgrounds") is True

def test_repeating_letters():
    assert is_isogram("look") is False
    assert is_isogram("banana") is False

def test_case_insensitivity():
    assert is_isogram("Adam") is False
    assert is_isogram("IsOgRam") is True

def test_long_isogram():
    assert is_isogram("subdermatoglyphic") is True