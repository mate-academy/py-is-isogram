import pytest
from app import main


@pytest.mark.parametrize(
    "word, expected",
    [
        ("", True),
        ("Adam", False),
        ("look", False),
        ("playgrounds", True),
    ],
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert main.is_isogram(word) == expected
