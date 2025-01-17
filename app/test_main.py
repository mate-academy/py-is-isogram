import pytest
from app.main import is_isogram


def test_if_isogram_is_empty_string() -> None:
    assert is_isogram(" ") is True


def test_if_isogram_do_not_contains_the_same_letters() -> None:
    assert is_isogram("playground") is True


def test_if_isogram_contains_the_same_letter() -> None:
    assert is_isogram("look") is False


def test_if_isogram_contains_different_registers() -> None:
    assert is_isogram("Adam") is False


if __name__ == "__main__":
    pytest.main()
