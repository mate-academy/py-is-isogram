import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, result",
    [
        pytest.param("playgrounds", True, id="'playgrounds' is isogram"),
        pytest.param("look", False, id="'look' contains 2 'o'"),
        pytest.param("Adam", False, id="'Adam' contains 2 'a'"),
        pytest.param("", True, id="empty string is isogram"),
    ]
)
def test_when_age_changes(
    word: str,
    result: bool
) -> None:
    assert (is_isogram(word) == result)
