import importlib
import pytest


mane = importlib.import_module("app.main")


def test_returns_bool() -> None:
    assert isinstance(mane.is_isogram(""), bool), \
        "function must return a boolean"


@pytest.mark.parametrize(
    "word, expected",
    [

        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),


        ("a", True),
        ("aba", False),
        ("abca", False),
        ("Dermatoglyphics", True),
        ("Subdermatoglyphic", True),
        ("Alphabet", False),
        ("Aa", False),
    ],
)
def test_examples_and_various_cases(word: str, expected: bool) -> None:
    assert mane.is_isogram(word) is expected


def test_case_insensitivity_explicit() -> None:

    assert mane.is_isogram("AbCdEfGhIjK") is True
    assert mane.is_isogram("AabcDEFgh") is False
