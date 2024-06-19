import pytest
from app.main import is_isogram


def test_is_isogram_empty_string() -> None:
    assert is_isogram("") is True


def test_is_isogram_single_character() -> None:
    assert is_isogram("a") is True
    assert is_isogram("B") is True


def test_is_isogram_isogram_words() -> None:
    assert is_isogram("playgrounds") is True
    assert is_isogram("subdermatoglyphic") is True
    assert is_isogram("abcdefg") is True


def test_is_isogram_non_isogram_words() -> None:
    assert is_isogram("look") is False
    assert is_isogram("Adam") is False
    assert is_isogram("hello") is False


def test_is_isogram_case_insensitivity() -> None:
    assert is_isogram("Adam") is False
    assert is_isogram("adam") is False
    assert is_isogram("AaA") is False
    assert is_isogram("Racecar") is False
    assert is_isogram("RaceCar") is False


if __name__ == "__main__":
    pytest.main()
