from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word, result",
    [
        pytest.param("playgrounds", True, id="'playgrounds' - should be True"),
        pytest.param("look", False, id="double 'OO' - should be False"),
        pytest.param("Adam", False, id="double 'aa' - should be False"),
        pytest.param("", True, id="empty string - should be True")
    ]
)
def test_is_isogram(word: str, result: bool) -> None:
    assert (
        is_isogram(word) == result
    )
