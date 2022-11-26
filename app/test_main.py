import pytest
from app.main import is_isogram


def test_should_return_true_when_word_is_empty_string() -> None:
    assert is_isogram("") is True


def test_should_return_expected_result_when_word_is_not_isogram() -> None:
    assert is_isogram("look") is False


def test_should_return_expected_result_when_word_is_isogram() -> None:
    assert is_isogram("playgrounds") is True


def test_should_return_expected_result_when_in_word_is_uppercase_letter()\
        -> None:
    assert is_isogram("Adam") is False


def test_should_raise_error_if_data_is_int() -> None:
    with pytest.raises(AttributeError):
        is_isogram(45)
