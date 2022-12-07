from app.main import is_isogram
import pytest


def test_raises_error_if_word_not_string() -> None:
    with pytest.raises(AttributeError):
        is_isogram(12345)


def test_returns_true_if_word_is_empty() -> None:
    assert is_isogram("") is True


def test_is_case_insensitive() -> None:
    assert is_isogram("bOok") is False


def test_returns_true_if_word_is_isogram() -> None:
    assert is_isogram("playgrounds") is True


def test_checks_nonconsecutive_letters() -> None:
    assert is_isogram("qwerqyQ") is False
