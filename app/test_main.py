from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word,result", [
        pytest.param(
            "", True,
            id="empty string should return True"
        ),
        pytest.param(
            "look", False,
            id="word look should return False"
        ),
        pytest.param(
            "Adam", False,
            id="function should be case insensitive"
        ),
        pytest.param(
            "playgrounds", True,
            id="test for a long word that returns True"
        ),
        pytest.param(
            "cOpYrIgHtABLe", True,
            id="test for case sensitivity in a long word"
        ),
        pytest.param(
            "      ", False,
            id="multiple spaces should return False"
        ),
    ]
)
def test_coin_combination(word: str, result: bool) -> None:
    assert is_isogram(word) == result
