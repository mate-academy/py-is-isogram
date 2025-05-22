from app.main import is_isogram
import pytest


def test_should_return_true_if_empty_string():
    word = ""
    assert is_isogram(word) is True


def test_should_return_false_if_small_and_big_letters():
    word = "Mama"
    assert is_isogram(word) is False


def test_should_return_true_if_correct():
    word = "England"
    assert is_isogram(word) is True


def test_should_return_false_if_incorrect():
    word = "america"
    assert is_isogram(word) is False


def test_should_raise_attributeerror():
    word = ["america"]
    with pytest.raises(AttributeError):
        assert is_isogram(word)
