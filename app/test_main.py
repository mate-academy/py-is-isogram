import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, bool_value",
    [
        pytest.param(
            "playgrounds", True,
            id="Should return True for playgrounds"
        ),
        pytest.param(
            "look", False,
            id="Should return False for consecutive letters"
        ),
        pytest.param(
            "Adam", False,
            id="Should return False"
               " for few non-consecutive letters of different case"
        ),
        pytest.param(
            "", True,
            id="Should return False"
               " for few non-consecutive letters of different case"
        ),
    ]
)
def test_is_the_word_isogram(word: str, bool_value: bool) -> None:
    assert is_isogram(word) == bool_value
