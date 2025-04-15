import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("Dermatoglyphics", True),
        ("aba", False),
        ("moOse", False),
        ("isogram", True),
        ("thumbscrew", True),
        ("", True),
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    """Test cases for is_isogram function."""
    assert is_isogram(word) == expected


@pytest.mark.parametrize(
    "word",
    [
        "abcdefghijklmnopqrstuvwxyz",
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ",
        "",
    ]
)
def test_is_isogram_edge_cases(word: str) -> None:
    """Test edge cases for is_isogram function."""
    if word == "abcdefghijklmnopqrstuvwxyz":
        assert is_isogram(word) is True
    elif word == "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        assert is_isogram(word) is True
    elif word == "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ":
        assert is_isogram(word) is False
    else:
        assert is_isogram(word) is True
