import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("", True),
        ("a", True),
        ("playgrounds", True),
        ("subdermatoglyphic", True),
        ("look", False),
        ("Adam", False),
    ],
)
def test_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) is expected
