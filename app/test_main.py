import pytest

from app.main import is_isogram


def test_isogram_is_case_insensitive() -> None:
    assert is_isogram("Dermatoglyphics") is True, (
        "String with different cases"
        " of the same letter is not an isogram."
    )


def test_empty_string_is_isogram() -> None:
    assert is_isogram("") is True, \
        "Empty string is an isogram."


def test_non_consecutive_letters_are_not_isogram() -> None:
    assert is_isogram("aba") is False, \
        "Not only consecutive letters are not an isogram."


def test_consecutive_letters_are_not_isogram() -> None:
    assert is_isogram("aa") is False, \
        "Consecutive same letters are not an isogram."


def test_single_character_is_isogram() -> None:
    assert is_isogram("a") is True, \
        "Single character string is an isogram."


def test_long_isogram_word() -> None:
    assert is_isogram("playgrounds") is True, \
        "'playgrounds' has no repeating letters and is an isogram."


def test_word_with_repeated_letter_mixed_case() -> None:
    assert is_isogram("Adam") is False, \
        "'Adam' has 'a' and 'A' which are the same letter — not an isogram."


def test_word_with_repeated_letter_same_case() -> None:
    assert is_isogram("look") is False, \
        "'look' has two 'o' letters and is not an isogram."


def test_uppercase_word_is_isogram() -> None:
    assert is_isogram("PYTHON") is True, \
        "Uppercase word with all unique letters is an isogram."


def test_uppercase_word_is_not_isogram() -> None:
    assert is_isogram("AABB") is False, \
        "Uppercase word with repeated letters is not an isogram."


@pytest.mark.parametrize("word,expected", [
    ("subdermatoglyphic", True),
    ("background", True),
    ("copyrights", True),
    ("isogram", True),
    ("lumberjacks", True),
    ("uncopyrightable", True),
    ("eleven", False),
    ("message", False),
    ("programming", False),
    ("Mama", False),
])
def test_parametrized_isogram_cases(word: str, expected: bool) -> None:
    assert is_isogram(word) is expected, (
        f"Expected is_isogram({word!r}) to be {expected}."
    )
