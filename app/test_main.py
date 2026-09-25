import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected",
    [
        pytest.param("", True, id="empty string is an isogram"),
        pytest.param("a", True, id="single letter is an isogram"),
        pytest.param("playgrounds", True, id="unique letters"),
        pytest.param("look", False, id="consecutive repeated letters"),
        pytest.param("letter", False, id="non-consecutive repeated letters"),
        pytest.param("Adam", False, id="same letter in different case"),
        pytest.param("aA", False, id="adjacent letters in different case"),
        pytest.param("Dermatoglyphics", True, id="mixed case unique letters"),
    ],
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) is expected
