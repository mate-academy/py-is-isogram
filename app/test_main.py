import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
    ]
)
def test_is_isogram_param(word: str, expected: bool) -> None:
    result = is_isogram(word)
    assert result == expected, (
        f"Expected is_isogram({word!r}) to return {expected}, got {result}"
    )


@pytest.mark.parametrize(
    "word, expected",
    [
        # single‐letter and two‐letter edge cases
        ("a", True),
        ("aa", False),
        ("ab", True),
        ("aA", False),  # case‐insensitive repeat

        # known long isograms
        ("Dermatoglyphics", True),
        ("subdermatoglyphic", True),

        # full alphabet
        ("abcdefghijklmnopqrstuvwxyz", True),

        # mixed‐case non‐isograms
        ("HelloWorld", False),   # 'l' appears 3 times
        ("Pythonista", False),   # 't' appears twice

        # random mid-length failures
        ("alphabet", False),     # 'a' twice
        ("Mississippi", False),  # many repeats
    ]
)
def test_additional_isogram_cases(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected, (
        f"Expected is_isogram({word!r}) == {expected}"
    )
