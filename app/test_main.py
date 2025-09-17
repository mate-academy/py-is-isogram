import pytest

from app.main import is_isogram

@pytest.mark.parametrize(
    "word, expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("Isogram", True),
        ("Aa", False),
        ("Ab", True),
    ]
)
def test_basic_cases(word: str, expected: bool) -> None:
    actual = is_isogram(word)
    assert actual == expected
    assert isinstance(actual, bool)
