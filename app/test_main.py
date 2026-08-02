import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("isogram", True),
        ("alphabet", False),
        ("Python", True),
        ("Case", True),
        ("case", True),
        ("Letter", False),
        ("AaBbCc", False),
    ],
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected


def test_isogram_single_letters() -> None:
    for letter in "abcdefghijklmnopqrstuvwxyz":
        assert is_isogram(letter) is True  # кожна буква сама по собі — ізограм


def test_isogram_upper_lower() -> None:
    assert is_isogram("aA") is False  # регістри не мають значення


def test_isogram_long_word() -> None:
    long_word: str = "abcdefghijklmnoqrstuvwyz"  # всі літери крім "p" і "x"
    assert is_isogram(long_word) is True


def test_empty_string() -> None:
    assert is_isogram("") is True
