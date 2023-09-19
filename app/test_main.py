import pytest
from app.main import is_isogram


def test_empty_string_is_isogram():
    assert is_isogram("") == True

def test_isogram_lowercase():
    assert is_isogram("isogram") == True

def test_isogram_uppercase():
    assert is_isogram("ISOGram") == True

def test_non_isogram():
    assert is_isogram("hello") == False

def test_mixed_case_isogram():
    assert is_isogram("AbCdEfG") == True

def test_non_alpha_characters():
    assert is_isogram("12345") == True
