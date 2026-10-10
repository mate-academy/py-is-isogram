import pytest

from app import main


@pytest.mark.parametrize(
    "word",
    [
        "",
        "a",
        "playgrounds",
        "abc",
        "Abc",
        "aBc",
    ],
)
def test_isograms(word: str) -> None:
    assert main.is_isogram(word) is True


@pytest.mark.parametrize(
    "word",
    [
        "look",
        "Adam",
        "aa",
        "aA",
        "Aa",
        "abca",
        "abcA",
        "aabc",
        "abcc",
        "abAb",
    ],
)
def test_not_isograms(word: str) -> None:
    assert main.is_isogram(word) is False
