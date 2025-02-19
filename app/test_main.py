import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected",
    [
        ("", True),
        ("a", True),
        ("aA", False),
        ("alphabet", False),
        ("children", True),
        ("abcdefghijklmnopqrstuvwxyz", True),
        ("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz", False),
    ]
)
def test_is_isogram(word, expected) -> None:
    assert is_isogram(word) is expected
