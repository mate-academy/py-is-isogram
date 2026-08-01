from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word, result",
    [
        pytest.param("playgrounds", True, id="Word is -> playgrounds"),
        pytest.param("look", False, id="Word is -> look"),
        pytest.param("Adam", False, id="Word is -> Adam"),
        pytest.param("", True, id="Empty string"),
    ]
)
def test_is_isogram(word: str, result: bool) -> None:
    assert is_isogram(word) == result
