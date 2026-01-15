import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word,isogram",
    [
        ("", True),
        ("apple", False),
        ("aPple", False),
        ("orange", True),
        ("Avocado", False),
        ("lemon1", True),
        ("lemon11", False),
    ]
)
def test_check_isogram(word: str, isogram: bool) -> None:
    assert is_isogram(word) == isogram
