import pytest
from app.main import is_isogram


@pytest.mark.parametrize("word, expected", [
    ("playgrounds", True),
    ("look", False),
    ("Adam", False),
    ("", True),

    ("Dermatoglyphics", True),
    ("Background", True),
    ("ISOGRAM", True),
    ("uncopyrightable", True),
    ("moose", False),
    ("subdermatoglyphic", True),
    ("Alphabet", False),

    ("hello", False),
    ("aabbcc", False),
    ("programming", False),
    ("six-year-old", False),
    ("abca", False),
    ("mama", False),

    ("Testing", False),
    ("Aa", False),
    ("BbC", False),
    ("cCb", False),
])
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected


def test_single_letter() -> None:
    assert is_isogram("a") is True
    assert is_isogram("A") is True
    assert is_isogram("z") is True


def test_two_unique_letters() -> None:
    assert is_isogram("ab") is True
    assert is_isogram("Ba") is True


def test_two_repeating_letters() -> None:
    assert is_isogram("aa") is False
    assert is_isogram("AA") is False
