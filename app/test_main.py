import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word,value",
    [
        pytest.param(
            "playgrounds",
            True,
            id="playgrounds is isogram"
        ),
        pytest.param(
            "look",
            False,
            id="look is not isogram"
        ),
        pytest.param(
            "Adam",
            False,
            id="Adam is not isogram"
        ),
        pytest.param(
            "",
            True,
            id="empty string is isogram"
        )
    ]
)
def test_is_isogram(
    word: str,
    value: bool,
) -> None:
    assert is_isogram(word) == value
