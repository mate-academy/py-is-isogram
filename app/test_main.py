import pytest

from app import main


@pytest.mark.parametrize(
    "word, expected",
    [
        ("playgrounds", True),
        ("isogram", True),
        ("look", False),
        ("aba", False),
    ],
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert main.is_isogram(word) is expected


def test_is_isogram_is_case_insensitive() -> None:
    assert main.is_isogram("Adam") is False


def test_empty_string_is_isogram() -> None:
    assert main.is_isogram("") is True
