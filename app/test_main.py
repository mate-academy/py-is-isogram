from app.main import is_isogram
import pytest


@pytest.mark.parametrize("word,expected", [
    pytest.param("playgrounds", True, id="isogram word"),
    pytest.param("look", False, id="has duplicate letters"),
    pytest.param("", True, id="empty string"),
    pytest.param("Adam", False, id="case insensitive duplicate letters"),
    pytest.param("Dermatoglyphics", True, id="case insensitive no duplicates"),
])
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
