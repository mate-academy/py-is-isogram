from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word, expected",
    [
        pytest.param(
            "",
            True,
            id="Should return 'True' for empty string"
        ),
        pytest.param(
            "Adam",
            False,
            id="Function should be case-insensitive"
        ),
        pytest.param(
            "playgrounds",
            True,
            id="Should return 'True' because 'playgrounds' is isogram"
        ),
        pytest.param(
            "BbB",
            False,
            id="Check non-consecutive letters"
        )
    ],
)
def test_get_coin_combination(word: str, expected: bool) -> None:

    assert is_isogram(word) == expected
