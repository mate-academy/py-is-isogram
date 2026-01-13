import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "words, expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
    ],
)


def test_is_isogram(words: str, expected: bool) -> None:
    assert is_isogram(words) == expected
