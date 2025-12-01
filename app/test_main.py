import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected",
    [
        ("", True),
        ("a", True),
        ("A", True),
        ("PYTEST", False),
        ("heLlo", False),
        ("HELLO", False),
        ("qq", False),
        ("222", False)
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
