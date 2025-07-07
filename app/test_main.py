import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word",
    [
        "playgrounds",
        "Python",
        "subdermatoglyphic",
    ],
)
def test_is_isogram_positive(word: str) -> None:
    assert is_isogram(word) is True


@pytest.mark.parametrize(
    "word",
    [
        "look",
        "Adam",
        "banana",
        "abca",
    ],
)
def test_is_isogram_negative(word: str) -> None:
    assert is_isogram(word) is False


@pytest.mark.parametrize(
    "word, expected",
    [
        ("", True),
        ("x", True),
        ("Aa", False),
        ("abcdefghijklmnopqrstuvwxyz", True),
        ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", True),
        ("abcdefghijklmnopqrstuvwxyz", True),
        ("aAbBcC", False),
        ("AbCdEfGhIjK", True),
    ],
)
def test_is_isogram_edge_cases(word: str, expected: bool) -> None:
    assert is_isogram(word) is expected
