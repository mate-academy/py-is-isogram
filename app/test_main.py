from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word, expected",
    [
        pytest.param(
            "playground", True,
            id="Should return True"
        ),
        pytest.param(
            "look", False,
            id="Should return False"
        ),
        pytest.param(
            "Adam", False,
            id="Should return False"
        ),
        pytest.param(
            "", True,
            id="Should return True"
        ),
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
