import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected_result",
    [
        pytest.param(
            "", True,
            id="should be True when empty sting"
        ),
        pytest.param(
            "Adam", False,
            id="should be case-insensitive"
        ),
        pytest.param(
            "playgrounds", True,
            id="should be True if no repeating letters"
        ),
        pytest.param(
            "adam", False,
            id="should be False if is repeating letters non-consecutive"
        ),
        pytest.param(
            "three", False,
            id="should be False if is repeating letters consecutive"
        )
    ]
)
def test_function(word: str, expected_result: bool) -> None:
    assert is_isogram(word) == expected_result
