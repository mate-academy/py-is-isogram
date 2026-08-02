import pytest

from app import main


@pytest.mark.parametrize(
    "word, expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),      # case-insensitive
        ("", True),           # empty string is an isogram
        ("a", True),
        ("abc", True),
        ("aba", False),       # non-consecutive repeat
        ("moOse", False),     # case-insensitive repeat
    ],
)
def test_examples_and_basic_cases(word: str, expected: bool) -> None:
    assert main.is_isogram(word) is expected


@pytest.mark.parametrize(
    "word",
    [
        "abcdefghijklmnopqrstuvwxyz",
        "Python",
        "World",
    ],
)
def test_returns_true_for_isograms(word: str) -> None:
    assert main.is_isogram(word) is True


@pytest.mark.parametrize(
    "word",
    [
        "letter",
        "Programming",
        "Mississippi",
    ],
)
def test_returns_false_for_non_isograms(word: str) -> None:
    assert main.is_isogram(word) is False


@pytest.mark.parametrize(
    "word",
    [
        "Aa",
        "BbB",
        "CcC",
    ],
)
def test_case_insensitive_behavior(word: str) -> None:
    assert main.is_isogram(word) is False
