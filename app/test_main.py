import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected_result",
    [
        pytest.param(
            "",
            True,
            id="should return `True` for an empty string",
        ),
        pytest.param(
            "acAdemy",
            False,
            id="should be case insensitive",
        ),
        pytest.param(
            "look",
            False,
            id=(
                "should return `False` when there "
                "are consecutive repeating letters"
            ),
        ),
        pytest.param(
            "playgrounds",
            True,
            id="should return `True` when word is an isogram",
        ),
    ],
)
def test_is_isogram(word: str, expected_result: bool) -> None:
    assert is_isogram(word) == expected_result
