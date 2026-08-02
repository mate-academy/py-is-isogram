import pytest
from app.main import is_isogram


def test_should_raise_error() -> None:
    with pytest.raises(AttributeError):
        is_isogram(15)


def test_data_is_empty() -> None:
    assert is_isogram("") is True


def test_with_repeating_letters() -> None:
    assert is_isogram("look") is False


def test_should_be_case_insensitive() -> None:
    assert is_isogram("Adam") is False


def test_true_value() -> None:
    assert is_isogram("playgrounds") is True
