from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word,expected_result",
    [
        pytest.param(
            "",
            True,
            id="test should return true when empty string"
        ),
        pytest.param(
            "playgrounds",
            True,
            id="test should return true when no repeating letters"
        ),
        pytest.param(
            "look",
            False,
            id="test should return false when repeating letters"
        ),
        pytest.param(
            "Adam",
            False,
            id="test function should be case insensitive"
        )
    ]
)
def test_no_repeat(word: str, expected_result: bool) -> None:
    assert is_isogram(word) == expected_result
