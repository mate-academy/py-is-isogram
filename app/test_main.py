import pytest

from app.main import is_isogram


def test_should_return_true_if_word_is_empty() -> None:
    assert is_isogram("") is True


def test_should_return_true_with_lower_words() -> None:
    assert is_isogram("come") is True


def test_should_return_true_with_upper_words() -> None:
    assert is_isogram("CoMe") is True


def test_should_return_false_if_word_is_not_isogram() -> None:
    assert is_isogram("comeback") is False


def test_should_return_false_with_upper_words_if_word_is_not_isogram() -> None:
    assert is_isogram("CoMeBacK") is False


def test_should_return_false_if_word_is_with_consecutive_letter() -> None:
    assert is_isogram("Aaaple") is False


def test_should_raise_error_if_word_is_not_string() -> None:
    with pytest.raises(AttributeError):
        is_isogram(5)
