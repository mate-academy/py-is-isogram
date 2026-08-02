import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected",
    [
        ("playgrounds", True),
        ("", True),
        ("isogram", True),
        ("look", False),
        ("Adam", False),
        ("alphabet", False),
        ("Machine", True),
        ("thumbscrewjapingly", True),
    ]
)
def test_is_isogram_various_words(word: str, expected: bool) -> None:
    assert is_isogram(word) is expected


def test_is_isogram_is_case_insensitive() -> None:
    assert is_isogram("Moose") is False


def test_is_isogram_returns_boolean() -> None:
    assert isinstance(is_isogram("test"), bool)
