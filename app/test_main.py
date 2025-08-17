import pytest

from app.main import is_isogram


def test_empty_string_is_isogram() -> None:
    assert is_isogram("") is True


def test_single_letter_is_isogram() -> None:
    assert is_isogram("a") is True


def test_simple_isogram() -> None:
    assert is_isogram("lamp") is True


def test_non_isogram_repeated_letter() -> None:
    assert is_isogram("letter") is False


def test_case_insensitivity() -> None:
    assert is_isogram("Alphabet") is False


def test_word_with_spaces_and_hyphens() -> None:
    assert is_isogram("six-year-old") is False


def test_all_unique_characters_long_string() -> None:
    assert is_isogram("abcdefghijklmnopqrstuvwxyz") is True


@pytest.mark.parametrize("word,expected", [
    ("isogram", True),
    ("hello", False),
    ("Python", True),
    ("moOse", False),
    ("subdermatoglyphic", True)
])
def test_parametrized_examples(word: str, expected: bool) -> None:
    assert is_isogram(word) is expected


def test_non_string_input_raises() -> None:
    with pytest.raises(AttributeError):
        is_isogram(None)
    with pytest.raises(AttributeError):
        is_isogram(123)
