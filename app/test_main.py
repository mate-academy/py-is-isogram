import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("  ", False),
        ("1Wake1", False),
        ("1234567", True),
        ("12121212", False)
    ]
)
def test_is_isogram(
        word: str,
        expected: bool
) -> None:
    assert is_isogram(word) == expected
