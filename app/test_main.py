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
        ("Alphabet", False),
        ("sixyearold", True),
        ("thumbscrewjapingly", True),
        ("aA", False),
        ("abcdeabc", False),
    ],
)
def test_is_isogram_cases(word: str, expected: bool) -> None:
    """Перевіряє різні випадки слів для is_isogram."""
    assert is_isogram(word) == expected


def test_isogram_empty_string() -> None:
    """Перевіряє, що порожній рядок є isogram."""
    assert is_isogram("") is True


def test_isogram_case_insensitivity() -> None:
    """Перевіряє, що функція нечутлива до регістру."""
    assert is_isogram("Aa") is False
    assert is_isogram("MoOn") is False
    assert is_isogram("Python") is True


def test_isogram_non_consecutive_repeats() -> None:
    """Перевіряє, що не лише послідовні повтори впливають на isogram."""
    assert is_isogram("aba") is False
    assert is_isogram("abcde") is True
    assert is_isogram("abCdeF") is True


def test_isogram_all_unique() -> None:
    """Перевіряє, що всі унікальні літери повертають True."""
    for word in ["qwerty", "zxcvbn", "asdfgh"]:
        assert is_isogram(word) is True


def test_isogram_single_letter() -> None:
    """Перевіряє, що одиночна літера є isogram."""
    assert is_isogram("a") is True
    assert is_isogram("Z") is True
