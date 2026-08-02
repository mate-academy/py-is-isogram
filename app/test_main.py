import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected",
    [
        pytest.param(
            "",
            True,
            id="Empty string is isogram"
        ),
        pytest.param(
            "playgrounds",
            True,
            id="playgrounds is isogram"
        ),
        pytest.param(
            "Adam",
            False,
            id="Adam not is isogram"
        ),
        pytest.param(
            "look",
            False,
            id="look is not isogram"
        )
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
