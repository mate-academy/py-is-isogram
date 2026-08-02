import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected",
    [
        ("hello", False),
        ("HeLlo", False),
        ("", True),
        ("Adam", False),
        ("playgrounds", True),
        ("Amno", True),
        ("legendary", False),
        ("lake", True),
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
