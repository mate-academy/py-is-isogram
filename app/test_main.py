import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected",
    [
        ("", True),
        ("PlayGrounds", True),
        ("look", False),
        ("Adam", False),
        ("a", True),
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
