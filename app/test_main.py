import pytest
from app.main import is_isogram  # ajuste o import conforme seu projeto

def test_empty_string_is_isogram() -> None:
    assert is_isogram("") is True

def test_all_unique_lowercase_letters() -> None:
    assert is_isogram("playgrounds") is True
    assert is_isogram("isogram") is True

def test_repeated_letters_lowercase() -> None:
    assert is_isogram("look") is False
    assert is_isogram("letter") is False

def test_repeated_letters_mixed_case() -> None:
    # M e m são a mesma letra
    assert is_isogram("Adam") is False
    assert is_isogram("AlAbA") is False

def test_single_letter_words() -> None:
    assert is_isogram("a") is True
    assert is_isogram("Z") is True

def test_case_insensitive() -> None:
    assert is_isogram("PlayGrounds") is True
    assert is_isogram("Look") is False
