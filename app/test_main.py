import pytest

from app.main import is_isogram


def test_should_return_true_when_playgrounds() -> None:
    assert is_isogram("playgrounds")


def test_should_return_true_when_empty_string() -> None:
    assert is_isogram("")


def test_should_return_true_when_isogram() -> None:
    assert is_isogram("uncopyrightable")


def test_should_return_false_when_letters_repeat() -> None:
    assert not is_isogram("look")


def test_should_return_false_ignoring_the_case() -> None:
    assert not is_isogram("Adam")


def test_test_should_raise_attribute_error() -> None:
    with pytest.raises(AttributeError):
        is_isogram(123)
