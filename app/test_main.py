import pytest

from app import main


@pytest.mark.parametrize(
    "word,expected",
    [
        ("", True),
        ("a", True),
        ("playgrounds", True),
        ("Dermatoglyphics", True),
        ("look", False),
        ("Adam", False),
        ("letter", False),
        ("isograms", False),
        ("aA", False),
    ],
    ids=[
        "empty string is isogram",
        "single letter is isogram",
        "word without repeats",
        "long word with uppercase letter",
        "consecutive repeating letters",
        "repeats with different case",
        "several repeating letters",
        "non-consecutive repeating letters",
        "same letter in both cases",
    ],
)
def test_should_check_if_word_is_isogram(word: str, expected: bool) -> None:
    assert main.is_isogram(word) is expected
