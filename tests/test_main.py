import pytest

from app.main import is_isogram


def test_should_be_true_if_empty_string():
    assert is_isogram("") is True


def test_case_insensitive():
    assert is_isogram("Adam") is False


def test_should_return_true_if_word_is_one_letter():
    assert is_isogram("I") is True


def test_should_return_true_if_word_is_isogram():
    assert is_isogram("python")
