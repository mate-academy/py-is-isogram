import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word,result",
    [
        pytest.param("playgrounds", True, id="'playgrounds' is isogram"),
        pytest.param("look", False, id="'look' is not isogram"),
        pytest.param("Adam", False, id="func should be case insensitive"),
        pytest.param("", True, id="the empty string is an isogram")
    ]
)
def test_is_isogram_values(word: str, result: bool) -> None:
    assert is_isogram(word) == result
