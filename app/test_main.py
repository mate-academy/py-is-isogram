import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected",
    [
        pytest.param(
            "playgrounds",
            True,
            id="valid isogram"),
        pytest.param(
            "look",
            False,
            id="consecutive duplicate"),
        pytest.param(
            "Adam",
            False,
            id="case-insensitive duplicate"),
        pytest.param(
            "",
            True,
            id="empty string")
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
