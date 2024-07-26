from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word_lower, result",
    [
        ("hide", True),
        ("Hidden", False),
        ("Hide", True),
        ("bag", True),
        ("Baga", False),
        ("Begging", False),
        ("", True),
        (" ", True),
        ("A", True),
        ("Aa", False),
    ]
)
def test_is_isogram(word_lower: str, result: bool) -> None:
    assert is_isogram(word_lower) == result
