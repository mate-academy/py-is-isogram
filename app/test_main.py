import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("", True),
        ("a", True),
        ("playgrounds", True),
        ("Machine", True),
        ("look", False),
        ("Adam", False),
        ("moOse", False),
        ("isIsogram", False),
        ("aba", False),
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) is expected
