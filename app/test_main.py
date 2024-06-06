from app.main import is_isogram
import pytest


def test_empty_string() -> None:
    assert is_isogram("") is True


def test_single_character() -> None:
    assert is_isogram("a") is True
    assert is_isogram("Z") is True


def test_isogram_lowercase() -> None:
    assert is_isogram("playgrounds") is True
    assert is_isogram("dermatoglyphics") is True


def test_non_isogram_lowercase() -> None:
    assert is_isogram("look") is False
    assert is_isogram("banana") is False


def test_isogram_mixed_case() -> None:
    assert is_isogram("Dermatoglyphics") is True
    assert is_isogram("Isogram") is True


def test_non_isogram_mixed_case() -> None:
    assert is_isogram("Adam") is False
    assert is_isogram("Look") is False


def test_isogram_with_repeated_characters() -> None:
    assert is_isogram("aba") is False
    assert is_isogram("moOse") is False
    assert is_isogram("isIsogram") is False


if __name__ == "__main__":
    pytest.main()
