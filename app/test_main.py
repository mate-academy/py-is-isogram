import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        pytest.param(
            "playgrounds",
            True,
            id="playgrounds is isogram"),
        pytest.param(
            "look",
            False,
            id="'look' is not isogram"),
        pytest.param(
            "Adam",
            False,
            id="'Adam' is not isogram"),
        pytest.param(
            '',
            True,
            id="Empty string is True"),
    ]
)
def test_is_isogram(word, expected):
    assert is_isogram(word) == expected
