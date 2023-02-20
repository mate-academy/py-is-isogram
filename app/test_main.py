import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,result",
    [
        pytest.param(
            "playgrounds",
            True,
            id="Word is isogram"
        ),
        pytest.param(
            "",
            True,
            id="Empty string is isogram"
        ),
        pytest.param(
            "Adam",
            False,
            id="Word is not isogram, despite of different cases"
        ),
        pytest.param(
            "look",
            False,
            id="Word is not isogram"
        )
    ]
)
def test_is_isogram(word: str, result: bool) -> None:
    assert is_isogram(word) == result
