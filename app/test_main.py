from app.main import is_isogram
import pytest

def test_isogram_examples():
    assert is_isogram('playgrounds') is True
    assert is_isogram('look') is False
    assert is_isogram('Adam') is False
    assert is_isogram('') is True

def test_case_insensitivity():
    assert is_isogram('MoM') is False
    assert is_isogram('aBcDeFg') is True

def test_non_letter_characters():
    with pytest.raises(ValueError):
        is_isogram('hello, world')
