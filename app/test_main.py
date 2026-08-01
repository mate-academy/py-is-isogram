import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected", [
        ("", True),
        ("Anna", False),
        ("Sam", True),
        ("eveline", False),
        ("sam", True)
    ]
)
def test_words_for_an_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected


def test_consecutive_letters_are_not_isogram() -> None:
    assert not is_isogram("river")


def test_non_consecutive_letters_are_not_isogram() -> None:
    assert not is_isogram("abbc")


def tests_isogram_is_case_insensitive() -> None:
    assert not is_isogram("Adam")
