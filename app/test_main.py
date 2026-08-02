from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word,expected",
    [
        pytest.param("playgrounds", True, id="isogram"),
        pytest.param("adam", False, id="not isogram"),
        pytest.param("look", False, id="not isogram with double letters"),
        pytest.param("Adam", False, id="not isogram with upper letter"),
        pytest.param("", True, id="empty")
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) is expected
