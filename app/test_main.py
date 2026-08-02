import pytest

from app.main import is_isogram


def test_empty_string_is_isogram() -> None:
    assert is_isogram("") is True


def test_single_letter_is_isogram() -> None:
    assert is_isogram("a") is True
    assert is_isogram("Z") is True


def test_simple_isograms() -> None:
    assert is_isogram("playgrounds") is True
    assert is_isogram("subdermatoglyphic") is True


def test_non_isograms() -> None:
    assert is_isogram("look") is False
    assert is_isogram("letter") is False
    assert is_isogram("Adam") is False


def test_case_insensitivity() -> None:
    assert is_isogram("Machine") is True
    assert is_isogram("mAchine") is True
    assert is_isogram("Alphabet") is False


@pytest.mark.parametrize(
    "word,expected", [
        ("background", True),
        ("downstream", True),
        ("reappear", False),
        ("Isogram", True),
        ("Programming", False),
    ]
)
def test_parametrized_isograms(word: str, expected: bool) -> None:
    assert is_isogram(word) is expected
