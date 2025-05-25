from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word, result",
    [
        pytest.param("playgrounds", True, id="no repeats"),
        pytest.param("look", False, id="2 repeats"),
        pytest.param("Adam", False, id="2 repeats"),
        pytest.param("", True, id="Empty")
    ]
)
def test_is_isogram(word: str, result: bool) -> None:
    assert is_isogram(word) == result
