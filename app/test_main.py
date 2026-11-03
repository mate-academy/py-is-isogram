import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word",
    [
        "",
        "a",
        "playgrounds",
        "abc",
        "Abc",
        "aBc",
        "Dermatoglyphics",
    ],
)
def test_is_isogram_should_return_true_for_isograms(word: str) -> None:
    assert is_isogram(word) is True


@pytest.mark.parametrize(
    "word",
    [
        "look",
        "aa",
        "abca",
        "abcdefga",
        "abcdefgg",
        "aabcdefg",
    ],
)
def test_is_isogram_should_return_false_for_repeated_letters(
    word: str,
) -> None:
    assert is_isogram(word) is False


@pytest.mark.parametrize(
    "word",
    ["Adam", "aA", "Aa", "abcdA", "Abcda", "mMabc"],
)
def test_is_isogram_should_be_case_insensitive(word: str) -> None:
    assert is_isogram(word) is False


@pytest.mark.parametrize("word", ["moOse", "isIsogram", "Mama"])
def test_is_isogram_should_detect_repeats_with_mixed_case(
    word: str,
) -> None:
    assert is_isogram(word) is False
