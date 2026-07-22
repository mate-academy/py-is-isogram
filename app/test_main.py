from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word, expected",
    [
        ("isogram", True),
        ("hello", False),
        ("", True),
        ("Dermatoglyphics", True),
        ("aba", False),
        ("moOse", False),
    ],
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) is expected


def test_is_isogram_empty_string() -> None:
    assert is_isogram("") is True


def test_is_isogram_case_insensitivity() -> None:
    assert is_isogram("Dermatoglyphics") is True
    assert is_isogram("dermatoglyphics") is True
    assert is_isogram("DERMATOGLYPHICS") is True


def test_is_isogram_non_isogram() -> None:
    assert is_isogram("hello") is False
    assert is_isogram("aba") is False
    assert is_isogram("moOse") is False


def test_is_isogram_single_character() -> None:
    assert is_isogram("a") is True
    assert is_isogram("A") is True


def test_is_isogram_with_spaces_and_hyphens() -> None:
    assert is_isogram("six-year-old") is False


def test_is_isogram_with_numbers() -> None:
    assert is_isogram("12345") is True
    assert is_isogram("112345") is False
