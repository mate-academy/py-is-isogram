import pytest

from app.main import is_isogram


def test_empty_string() -> None:
    assert is_isogram('') is True


def test_capital_letter_false() -> None:
    assert is_isogram('Adam') is False


def test_main_true() -> None:
    assert is_isogram('playgrounds') is True


def test_main_false() -> None:
    assert is_isogram('look') is False


def test_capital_letter_true() -> None:
    assert is_isogram('True') is True
