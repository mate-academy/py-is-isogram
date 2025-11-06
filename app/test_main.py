import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("Aa", False),
        ("", True),
        ("Background", True),
        ("Alphabet", False),
        ("moOse", False),
        ("x", True),
    ]
)
def test_is_isogram_cases(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
