import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("isogram", True),
        ("Isogram", True),
        ("hello", False),
        ("Python", True),
        ("alphabet", False)
    ]
)
def test_is_isogram(word: str, expected: list) -> None:
    assert is_isogram(word) == expected
