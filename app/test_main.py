import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("playgrounds", True),   # 'playgrounds' is an isogram
        ("look", False),         # 'look' contains repeating 'o'
        ("Adam", False),         # 'Adam' contains repeating 'a'
        ("", True),              # An empty string is an isogram
        ("isogram", True),       # A typical isogram word
        ("repeat", False),       # 'repeat' contains repeating 'e'
        ("abcdefghij", True),    # A sequence of unique letters
        ("aAa", False),          # 'aAa' is not an isogram
    ],
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected, f"Failed for word: '{word}'"
