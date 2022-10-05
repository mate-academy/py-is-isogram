import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "checked_string, result",
    [
        pytest.param(
            "playgrounds",
            True,
            id="should return True if it has no repeating letters"
        ),
        pytest.param(
            "look",
            False,
            id="should return False if it has  repeating letters"
        ),
        pytest.param(
            "Adam",
            False,
            id="should be case-insensitive"
        ),
        pytest.param(
            "",
            True,
            id="should return True if input is empty"
        ),
    ]
)
def test_correct_output(checked_string: str, result: bool) -> None:
    assert is_isogram(checked_string) is result
