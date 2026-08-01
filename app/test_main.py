import pytest
from app.main import is_isogram


TEST_CASES = [
    ("playgrounds", True),
    ("", True),
    ("a", True),
    ("Dermatoglyphics", True),
    ("six", True),

    ("look", False),
    ("Adam", False),
    ("Banana", False),
    ("Testing", False),
    ("moose", False),
    ("uncopyrightable", True),
    ("alphabetical", False)
]


@pytest.mark.parametrize("word, expected", TEST_CASES)
def test_is_isogram(word: str, expected: bool) -> None:
    actual = is_isogram(word)
    assert actual == expected, (f"Input: '{word}', "
                                f"Expected: {expected}, Got: {actual}")


def test_single_capital_repeat() -> None:
    assert is_isogram("Aa") is False
    assert is_isogram("mM") is False


def test_multiple_non_consecutive_repeat() -> None:
    assert is_isogram("programming") is False
