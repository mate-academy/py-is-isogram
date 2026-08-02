import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected",
    [
        pytest.param(
            "playgrounds", True,
            id="is isogram",
        ),
        pytest.param(
            "look", False,
            id="not a isogram",
        ),
        pytest.param(
            "Adam", False,
            id="not a isogram",
        ),
        pytest.param(
            "", True,
            id="empty string should be True"
        ),
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
