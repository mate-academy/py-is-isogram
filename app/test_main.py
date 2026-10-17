import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected",
    [
        pytest.param("", True, id="empty string is an isogram"),
        pytest.param("a", True, id="single letter is an isogram"),
        pytest.param("playgrounds", True, id="word without repeats"),
        pytest.param("look", False, id="consecutive repeating letters"),
        pytest.param("letter", False, id="non-consecutive repeating letters"),
        pytest.param("Adam", False, id="case-insensitive repeating letters"),
        pytest.param("PlayGrounds", True, id="mixed case without repeats"),
    ],
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) is expected
