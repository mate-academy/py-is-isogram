from app.main import is_isogram
import pytest

TEST_CASES = [
    ("", True),
    ("a", True),
    ("isogram", True),
    ("eleven", False),
    ("subdermatoglyphic", True),
    ("thunder", True),
    ("python", False),
    ("Aleph", False),
]


@pytest.mark.parametrize("word, expected", TEST_CASES)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
