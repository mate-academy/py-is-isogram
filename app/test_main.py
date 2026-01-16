import pytest
from app.main import is_isogram
from collections import Counter


def test_should_return_bool() -> None:
    assert isinstance(is_isogram("look"), bool)


def test_should_return_true_if_all_letter_meet_once_in_the_word() -> None:
    word = "playgrounds"
    dict_of_word = Counter(word)
    check = False
    if all(dict_of_word.values()) == 1:
        check = True
    assert is_isogram("playgrounds") == check


def test_function_should_be_case_insensitive_a_is_the_same_letter() -> None:
    word_1 = "NazAr"
    word_2 = "Nazar"
    big_letter = is_isogram(word_1)
    small_letter = is_isogram(word_2)
    assert big_letter == small_letter


def test_the_empty_string_is_an_isogram() -> None:
    assert is_isogram("") is True


def test_not_only_consecutive_letters_are_not_an_isogram() -> None:
    assert is_isogram("Adam") is False


def test_consecutive_letters_are_not_isogram() -> None:
    assert is_isogram("ff") is False


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    with pytest.raises(AttributeError):
        is_isogram(0)
