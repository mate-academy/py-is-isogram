import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        pytest.param(
            "", True,
            id="Empty string is an isogram"
        ),
        pytest.param(
            "Adam", False,
            id="String with different cases of the same letter is not an isogram"
        ),
        pytest.param(
            "playgrounds", True,
            id="Should return True when each letter occurs once"
        ),
        pytest.param(
            "look", False,
            id="Should return False when letter occurs more than once"
        )
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
