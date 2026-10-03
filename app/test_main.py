import pytest

from app import main


@pytest.mark.parametrize(
    "word,expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
    ],
)
def test_is_isogram_examples_from_task(word: str, expected: bool) -> None:
    assert main.is_isogram(word) is expected


def test_is_isogram_is_case_insensitive() -> None:
    assert main.is_isogram("Adam") is False


def test_empty_string_is_an_isogram() -> None:
    assert main.is_isogram("") is True


def test_repeated_letters_not_next_to_each_other_is_not_isogram() -> None:
    assert main.is_isogram("aba") is False


def test_repeated_letters_next_to_each_other_is_not_isogram() -> None:
    assert main.is_isogram("look") is False
