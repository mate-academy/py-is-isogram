import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("AleksA", False),
        ("", True),
        ("isogram", True),
        ("eleven", False),
        ("subdermatoglyphic", True),
        ("aba", False),
        ("fqpcl", True),
    ],
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
