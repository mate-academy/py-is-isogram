import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("Dermatoglyphics", True),
        ("moose", False),
        ("aba", False),
    ],
)
def test_is_isogram(word: str, expected: bool) -> None:
    """Test is_isogram with various words."""
    assert is_isogram(word) == expected
