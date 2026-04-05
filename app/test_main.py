import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("Alphabet", False),
        ("isogram", True),
        ("thumbscrewjapingly", True),
        ("aba", False),
        ("moOse", False),
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) is expected


def test_is_isogram_case_insensitivity() -> None:
    assert is_isogram("AbC") is True
    assert is_isogram("Aa") is False
