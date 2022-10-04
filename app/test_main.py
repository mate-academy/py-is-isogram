import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected",
    [
        pytest.param(
            "", True,
            id="should return True if string is empty"),
        pytest.param(
            "playgrounds", True,
            id="should return True if string have no repeating letters"),
        pytest.param(
            "look", False,
            id="should return False if string have repeating letters"
        ),
        pytest.param(
            "Adam", False,
            id="should return False because function should be case-insensitive"
        )
    ]
)
def test_is_isogram(word, expected):
    assert is_isogram(word) == expected
