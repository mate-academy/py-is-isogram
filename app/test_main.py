import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected",
    [
        ("playgrounds", True),
        ("", True),
        ("lumberjack", True),
        ("background", True),
        ("downstream", True),
        ("look", False),
        ("Adam", False),
        ("banana", False),
        ("Moose", False),
    ],
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) is expected
