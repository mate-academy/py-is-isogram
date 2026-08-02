import pytest

from app.main import is_isogram


def test_should_return_true_if_empty_string_passed() -> None:
    assert is_isogram("") is True


def test_should_return_false_if_letter_exist_in_diff_case() -> None:
    assert is_isogram("Adam") is False


def test_should_return_false_if_nonconsecutive_letters_isogram() -> None:
    assert is_isogram("look") is False


def test_should_raise_error_when_passed_not_string_type() -> None:
    with pytest.raises(AttributeError):
        is_isogram(4)
