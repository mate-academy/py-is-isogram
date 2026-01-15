import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected",
    [
        pytest.param("", True, id="empty string is isogram"),
        pytest.param("playgrounds", True, id="is isogram"),
        pytest.param("look", False, id="is not isogram"),
        pytest.param("Adam", False, id="should be case-insensitive")
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
