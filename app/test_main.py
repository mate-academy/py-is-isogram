import pytest

import app.main as main_module


@pytest.mark.parametrize("word,expected", [
    ("", True),
    ("a", True),
    ("playgrounds", True),
    ("abcdefghijklmnopqrstuvwxyz", True),
    ("look", False),
    ("Adam", False),
    ("hello", False),
    ("aA", False),
    ("Dermatoglyphics", True),
    ("isogram", True),
    ("aba", False),
])
def test_is_isogram(word: str, expected: bool) -> None:
    assert main_module.is_isogram(word) == expected


def test_empty_string_is_isogram() -> None:
    assert main_module.is_isogram("") is True


def test_case_insensitive_same_letter_not_isogram() -> None:
    assert main_module.is_isogram("Aa") is False


def test_case_insensitive_different_letters_is_isogram() -> None:
    assert main_module.is_isogram("Ab") is True


def test_returns_bool() -> None:
    assert isinstance(main_module.is_isogram("word"), bool)
