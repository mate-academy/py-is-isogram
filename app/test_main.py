import pytest
from app.main import is_isogram


@pytest.mark.parametrize("word, expected", [
    ("", True),
    ("z", True),
    ("playgrounds", True),
    ("look", False),
    ("alphabet", False),
    ("Adam", False),
    ("Aa", False),
])
def test_is_isogram_examples(word: str, expected: bool) -> None:
    assert is_isogram(word) is expected


def test_case_insensitive() -> None:
    assert is_isogram("Aa") is False


def test_empty_string_is_isogram() -> None:
    assert is_isogram("") is True


def test_non_consecutive_duplicate_letters() -> None:
    assert is_isogram("alphabet") is False
