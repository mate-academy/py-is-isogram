import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected",
    [
        pytest.param("", True, id="empty string"),
        pytest.param("a", True, id="single character"),
        pytest.param("look", False, id="consecutive duplicate"),
        pytest.param("Playgrounds", True, id="valid isogram"),
        pytest.param("Adam", False, id="case-insensitive duplicate"),
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
