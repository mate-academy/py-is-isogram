import pytest

from app.main import is_isogram


def test_normal_true() -> None:
    assert is_isogram("AbCDEfG") is True


def test_normal_false() -> None:
    assert is_isogram("cAA") is False


def test_not_consecutive_letters() -> None:
    assert is_isogram("abcb") is False


def test_empty_string() -> None:
    assert is_isogram("") is True


def test_attribute_error() -> None:
    with pytest.raises(AttributeError):
        is_isogram(1)
