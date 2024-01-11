from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "initial_input,expected_result",
    [
        pytest.param(
            "playgrounds", True,
            id="should return correct value"
        ),
        pytest.param(
            "Adam", False,
            id="should be case-insensitive"
        ),
        pytest.param(
            "", True,
            id="should return True, when initial input is empty string"
        ),
        pytest.param(
            "abca", False,
            id="should return False with non consecutive letters"
        )
    ]
)
def test_should_return_correct_value(
        initial_input: str,
        expected_result: bool
) -> None:
    assert is_isogram(initial_input) == expected_result
