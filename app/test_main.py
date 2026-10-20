import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("", True),
        ("playgrounds", True),
        ("isogram", True),
        ("cat", True),
        ("look", False),
        ("banana", False),
        ("Adam", False),
        ("MoOM", False),
    ],
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
