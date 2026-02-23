import pytest

from app.main import is_isogram  # або заміни main на свій файл


@pytest.mark.parametrize(
    "word, expected",
    [
        ("playgrounds", True),   # усі літери різні
        ("look", False),         # дві "o"
        ("Adam", False),         # "a" повторюється (регістр ігнорується)
        ("", True),              # порожній рядок
        ("isogram", True),
        ("alphabet", False),     # "a" повторюється
        ("Python", True),
        ("Case", True),
        ("case", True),
        ("Letter", False),       # "t" повторюється
        ("AaBbCc", False),       # "a" і "A" однакові
    ],
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected


def test_isogram_single_letters() -> None:
    for c in "abcdefghijklmnopqrstuvwxyz":
        assert is_isogram(c) is True  # кожна буква сама по собі — ізограм


def test_isogram_upper_lower() -> None:
    assert is_isogram("aA") is False  # регістри не мають значення


def test_isogram_long_word() -> None:
    word = "abcdefghijklmnoqrstuvwyz"  # всі літери крім "p" і "x"
    assert is_isogram(word) is True


def test_empty_string() -> None:
    assert is_isogram("") is True