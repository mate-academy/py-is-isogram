from __future__ import annotations

import pytest

from app.main import is_isogram


def test_empty_string_is_isogram() -> None:
    assert is_isogram("") is True


def test_one_letter_word_is_isogram() -> None:
    assert is_isogram("a") is True


def test_word_without_repeated_letters_is_isogram() -> None:
    assert is_isogram("playgrounds") is True


def test_word_with_repeated_letters_is_not_isogram() -> None:
    assert is_isogram("look") is False


def test_word_with_repeated_letters_in_different_cases() -> None:
    assert is_isogram("Adam") is False


def test_uppercase_and_lowercase_are_compared_case_insensitively() -> None:
    assert is_isogram("MoOse") is False


def test_word_with_repeated_uppercase_letter_is_not_isogram() -> None:
    assert is_isogram("ALPHA") is False


def test_word_with_all_lowercase_letters_is_isogram() -> None:
    assert is_isogram("background") is True


def test_consecutive_repeated_letters_are_not_isogram() -> None:
    assert is_isogram("letter") is False


def test_non_consecutive_repeated_letters_are_not_isogram() -> None:
    assert is_isogram("moose") is False


def test_long_word_without_repeated_letters_is_isogram() -> None:
    assert is_isogram("uncopyrightable") is True


@pytest.mark.parametrize(
    "word, expected",
    [
        ("", True),
        ("a", True),
        ("A", True),
        ("aa", False),
        ("Aa", False),
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("MoOse", False),
        ("ALPHA", False),
        ("background", True),
        ("letter", False),
        ("isogram", True),
        ("uncopyrightable", True),
    ],
)
def test_is_isogram_returns_expected_result(
    word: str,
    expected: bool,
) -> None:
    assert is_isogram(word) == expected
