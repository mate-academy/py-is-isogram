import pytest
from app.main import is_isogram


def test_is_isogram_empty_string() -> None:
    assert is_isogram("") is True


def test_is_isogram_single_letter() -> None:
    assert is_isogram("a") is True
    assert is_isogram("Z") is True
    assert is_isogram("m") is True


def test_is_isogram_valid_isograms() -> None:
    assert is_isogram("playgrounds") is True
    assert is_isogram("word") is True
    assert is_isogram("abc") is True
    assert is_isogram("ABCDEF") is True
    assert is_isogram("background") is True
    assert is_isogram("mighty") is True


def test_is_isogram_invalid_isograms() -> None:
    assert is_isogram("look") is False
    assert is_isogram("hello") is False
    assert is_isogram("book") is False
    assert is_isogram("letter") is False
    assert is_isogram("programming") is False
    assert is_isogram("twelve") is False
    assert is_isogram("galaxy") is False


def test_is_isogram_case_insensitive() -> None:
    assert is_isogram("Adam") is False
    assert is_isogram("Mom") is False
    assert is_isogram("AbC") is True
    assert is_isogram("AbCa") is False
    assert is_isogram("Test") is False
    assert is_isogram("AbcD") is True


def test_is_isogram_mixed_case_valid() -> None:
    assert is_isogram("Uncopyrightable") is True
    assert is_isogram("Background") is True
    assert is_isogram("Exhausting") is True


def test_is_isogram_adjacent_duplicates() -> None:
    assert is_isogram("good") is False
    assert is_isogram("seen") is False
    assert is_isogram("door") is False
    assert is_isogram("book") is False


def test_is_isogram_non_adjacent_duplicates() -> None:
    assert is_isogram("civic") is False
    assert is_isogram("level") is False
    assert is_isogram("radar") is False
    assert is_isogram("refer") is False


def test_is_isogram_long_words() -> None:
    assert is_isogram("uncopyrightables") is True
    assert is_isogram("dermatoglyphics") is True
    assert is_isogram("subdermatoglyphic") is True
    assert is_isogram("troublemakings") is True


def test_is_isogram_alphabet() -> None:
    assert is_isogram("abcdefghijklmnopqrstuvwxyz") is True
    assert is_isogram("abcdefghijklmnopqrstuvwxyza") is False


@pytest.mark.parametrize("word, expected", [
    ("", True),
    ("a", True),
    ("playgrounds", True),
    ("look", False),
    ("Adam", False),
    ("word", True),
    ("hello", False),
    ("AbC", True),
    ("Test", False),
    ("background", True),
    ("programming", False),
    ("Uncopyrightable", True),
])
def test_is_isogram_examples(word: str, expected: bool) -> None:
    assert is_isogram(word) is expected
