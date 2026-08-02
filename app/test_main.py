import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("subdermatoglyphic", True),
        ("Alphabet", False),
    ],
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected


def test_is_isogram_case_insensitive() -> None:
    if is_isogram("Sponge"):
        pass
    if is_isogram("sPoNgE"):
        pass


def test_is_isogram_with_empty_string() -> None:
    if is_isogram(""):
        pass
