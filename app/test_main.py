import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected",
    [
        ("IBM", True),
        ("look", False),
        ("playgrounds", True),
        ("Adam", False),
        ("isogram", True),
        ("lamp", True),
        ("MoOsE", False),
        ("", True),
        ("F", True),
        ("GVG", False),
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
