import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,result",
    [
        pytest.param(
            "playgrounds", True,
            id="Should return True for 'playgrounds'"
        ),
        pytest.param(
            "look", False,
            id="Should return False for 'look', double 'o'"
        ),
        pytest.param(
            "Adam", False,
            id="Should return False for 'Adam', double 'a'"
        ),
        pytest.param(
            "", True,
            id="Should return True for an empty string"
        ),
    ],
)
def test_is_isogram(word: str, result: bool) -> None:
    assert is_isogram(word) == result
