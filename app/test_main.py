import pytest

import app.main as main_module


@pytest.mark.parametrize("word, expected", [
    ("", True),
    ("a", True),
    ("playgrounds", True),
    ("look", False),
    ("Adam", False),
    ("hello", False),
    ("Mama", False),
    ("Dermatoglyphics", True),
    ("moOse", False),
])
def test_is_isogram(word: str, expected: bool) -> None:
    assert main_module.is_isogram(word) is expected


def test_empty_string_is_isogram() -> None:
    assert main_module.is_isogram("") is True


def test_consecutive_letters_are_not_isogram() -> None:
    assert main_module.is_isogram("moon") is False


def test_non_consecutive_letters_are_not_isogram() -> None:
    assert main_module.is_isogram("abac") is False


def test_isogram_is_case_insensitive() -> None:
    assert main_module.is_isogram("Mama") is False


@pytest.mark.parametrize("word", [
    123,
    None,
    ["word"],
])
def test_invalid_input_raises_exception(word: str) -> None:
    with pytest.raises(Exception):
        main_module.is_isogram(word)
