import pytest
from app.main import is_isogram


def test_should_return_attribute_error() -> None:
    with pytest.raises(AttributeError):
        is_isogram(["car"])


def test_should_return_true_if_input_is_empty_string() -> None:
    assert is_isogram("") is True


def test_should_return_false_if_letters_are_duplicating() -> None:
    assert is_isogram("look") is False
    assert is_isogram("Adam") is False
    assert is_isogram("Academy") is False


def test_should_return_true_if_word_is_isogram() -> None:
    assert is_isogram("playgrounds") is True
    assert is_isogram("Mate") is True
