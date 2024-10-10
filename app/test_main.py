import pytest
from app.main import is_isogram


@pytest.mark.parametrize("word, expected", [
    ("playgrounds", True),
    ("look", False),
    ("Adam", False),
    ("", True),
    ("isogram", True),
    ("eleven", False),
    ("subdermatoglyphic", True),
    ("AlPhAbEt", False),
    ("thumbscrew-japingly", True),
    ("a", True),
    ("moOse", False),
])
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) is expected


def test_is_isogram_case_insensitive() -> None:
    assert not is_isogram("Alphabet")


def test_is_isogram_with_empty_string() -> None:
    assert is_isogram("") is True
