import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("", True),
        ("a", True),
        ("A", True),
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("isogram", True),
        ("machine", True),
        ("background", True),
        ("subdermatoglyphic", True),
        ("hello", False),
        ("letter", False),
        ("book", False),
        ("apple", False),
        ("banana", False),
        ("alphabet", False),
        ("Aa", False),
        ("aA", False),
        ("AbC", True),
        ("aBcA", False),
        ("ABCabc", False),
        ("Python", True),
        ("Mississippi", False),
        ("abcdefghijklmnopqrstuvwxyz", True),
        ("abcdefghijklmnopqrstuvwxyza", False),
    ]
)
def test_is_isogram_expected_results(
    word: str,
    expected: bool
) -> None:
    assert is_isogram(word) is expected


def test_is_isogram_returns_boolean() -> None:
    result = is_isogram("unique")
    assert isinstance(result, bool)


def test_is_isogram_consecutive_repeated_letters() -> None:
    assert is_isogram("coffee") is False


def test_is_isogram_nonconsecutive_repeated_letters() -> None:
    assert is_isogram("abca") is False


def test_is_isogram_case_insensitivity() -> None:
    assert is_isogram("aBcDeF") is True
    assert is_isogram("aBcDefA") is False
