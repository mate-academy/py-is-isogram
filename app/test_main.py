import pytest

from app import main


@pytest.mark.parametrize(
    "word",
    [
        "playgrounds",
        "",
        "a",
        "A",
        "abc",
        "Abc",
        "aBcDe",
        "Isogram",
        "background",
    ],
)
def test_should_return_true_for_isograms(word: str) -> None:
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
        "moOse",
        "letter",
        "isograms",
    ],
)
def test_should_return_false_for_non_isograms(word: str) -> None:
    assert main.is_isogram(word) is False


@pytest.mark.parametrize(
    "word",
    ["aab", "baa", "abba", "abAb", "ABCDEFa"],
)
def test_should_detect_consecutive_and_non_consecutive_repeats(
    word: str
) -> None:
    assert main.is_isogram(word) is False


@pytest.mark.parametrize(
    "word_lower,word_upper",
    [("playgrounds", "PLAYGROUNDS"), ("look", "LOOK"), ("adam", "ADAM")],
)
def test_result_should_not_depend_on_case(
    word_lower: str,
    word_upper: str
) -> None:
    assert main.is_isogram(word_lower) is main.is_isogram(word_upper)
