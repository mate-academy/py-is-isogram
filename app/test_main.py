from app.main import is_isogram

import pytest


@pytest.mark.parametrize(
    "word, expected",
    [
        pytest.param(
            "playgrounds", True,
            id="Word is isogram"
        ),
        pytest.param(
            "look", False,
            id="Word is not isogram"
        ),
        pytest.param(
            "Adam", False,
            id="Capitalize word is not isogram"
        ),
        pytest.param(
            "", True,
            id="Empty string is isogram"
        )
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
