from app.main import is_isogram
import pytest


def test_is_isogram_with_empty_string() -> None:
    assert is_isogram("") is True


def test_is_isogram_with_unique_letters() -> None:
    assert is_isogram("playgrounds") is True


def test_is_isogram_with_repeated_letters() -> None:
    assert is_isogram("look") is False


def test_is_isogram_with_mixed_case() -> None:
    assert is_isogram("Adam") is False


def test_is_isogram_with_mixed_case_unique_letters() -> None:
    assert is_isogram("Mma") is False


if __name__ == "__main__":
    pytest.main()
