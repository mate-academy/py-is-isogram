import pytest
from app.main import is_isogram


def test_empty_string() -> None:
    assert is_isogram("") is True


def test_single_letter() -> None:
    assert is_isogram("a") is True


def test_all_unique_lowercase() -> None:
    assert is_isogram("playgrounds") is True


def test_repeated_letters_consecutive() -> None:
    assert is_isogram("look") is False


def test_repeated_letters_non_consecutive() -> None:
    assert is_isogram("banana") is False


def test_case_insensitive_check() -> None:
    assert is_isogram("Adam") is False


def test_all_unique_uppercase() -> None:
    assert is_isogram("WORLD") is True


def test_mixed_case_unique() -> None:
    assert is_isogram("Python") is True


@pytest.mark.parametrize(
    "word, expected",
    [
        ("Anton", False),
        ("isogram", True),
        ("Ukraine", True),
        ("DevOps", True),
    ],
)
def test_parametrized_examples(word: str, expected: bool) -> None:
    assert is_isogram(word) is expected
