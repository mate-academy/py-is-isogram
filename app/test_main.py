from app.main import is_isogram
import pytest


def test_false_if_same_letter_in_different_registers() -> None:
    word = "Adam"
    assert is_isogram(word) is False


def test_false_if_same_letter_in_same_registers() -> None:
    word = "look"
    assert is_isogram(word) is False


def test_true_if_word_is_empty_str() -> None:
    word = ""
    assert is_isogram(word) is True


def test_error_if_word_is_not_str() -> None:
    with pytest.raises(AttributeError):
        word = 123
        is_isogram(word)
