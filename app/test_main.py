import pytest
from app.main import is_isogram  # Adjust the import path based on your project structure


def test_empty_string() -> None:
    assert is_isogram('') is True


def test_single_letter() -> None:
    assert is_isogram('a') is True


def test_isogram_lowercase() -> None:
    assert is_isogram('playgrounds') is True


def test_isogram_mixed_case() -> None:
    assert is_isogram('Dermatoglyphics') is True


def test_not_isogram_consecutive() -> None:
    assert is_isogram('look') is False


def test_not_isogram_non_consecutive() -> None:
    assert is_isogram('hello') is False


def test_isogram_with_uppercase() -> None:
    assert is_isogram('Background') is True


def test_not_isogram_mixed_case() -> None:
    assert is_isogram('Adam') is False


def test_isogram_all_same_letters() -> None:
    assert is_isogram('Aaa') is False


def test_isogram_with_mixed_case_duplicates() -> None:
    assert is_isogram('Alphabet') is False


if __name__ == "__main__":
    pytest.main()
