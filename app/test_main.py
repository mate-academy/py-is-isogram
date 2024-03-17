from app.main import is_isogram
import pytest


def test_right() -> None:
    assert is_isogram("Oles") is True


def test_consecutive_letters() -> None:
    assert is_isogram("aaa") is False


def test_should_return_bool() -> None:
    result = is_isogram("Mate")
    assert isinstance(result, bool)


def test_empty_string() -> None:
    assert is_isogram("") is True


def test_double_lower_letter() -> None:
    assert is_isogram("academy") is False


def test_double_upper_letter() -> None:
    assert is_isogram("LVIV") is False


def test_upper_lower_letter() -> None:
    assert is_isogram("Ludmyla") is False
