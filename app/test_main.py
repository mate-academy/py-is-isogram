import pytest

from app import main


def is_isogram(word: str) -> bool:
    return main.is_isogram(word)


def test_word_without_repeating_letters_is_isogram() -> None:
    assert is_isogram("playgrounds") is True


def test_word_with_repeating_letters_is_not_isogram() -> None:
    assert is_isogram("look") is False


def test_case_insensitive_repeating_letters_is_not_isogram() -> None:
    assert is_isogram("Adam") is False


def test_empty_string_is_isogram() -> None:
    assert is_isogram("") is True


def test_single_letter_is_isogram() -> None:
    assert is_isogram("a") is True


def test_all_same_letter_is_not_isogram() -> None:
    assert is_isogram("aaaa") is False


def test_two_different_letters_is_isogram() -> None:
    assert is_isogram("ab") is True


def test_uppercase_word_without_repeats_is_isogram() -> None:
    assert is_isogram("ISOGRAM") is True


def test_mixed_case_word_with_repeats_is_not_isogram() -> None:
    assert is_isogram("Alphabet") is False


def test_word_with_repeats_at_the_end_is_not_isogram() -> None:
    assert is_isogram("bookkeeper") is False


def test_uppercase_word_with_distinct_letters_is_isogram() -> None:
    assert is_isogram("OXYGEN") is True


def test_isogram_with_full_lowercase_and_uppercase_pair() -> None:
    assert is_isogram("subdermatoglyphic") is True


@pytest.mark.parametrize(
    "word, expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("Dermatoglyphics", True),
        ("moOse", False),
    ],
)
def test_is_isogram_parametrized(word: str, expected: bool) -> None:
    assert is_isogram(word) is expected
