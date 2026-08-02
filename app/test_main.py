import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "string, expected",
    [
        pytest.param(
            "", True, id="test_with_empty_string_true"
        ),
        pytest.param(
            "look", False, id="test_with_repeating_letter_together_false"
        ),
        pytest.param(
            "adam", False, id="test_with_repeating_letter_not_together_false"
        ),
        pytest.param(
            "Adam", False, id="test_with_different_cases_false"
        ),
        pytest.param(
            "playgrounds", True, id="test_with_no_repeating_true"
        )
    ]
)
def test_is_isogram(string: str, expected: bool) -> bool:
    assert is_isogram(string) is expected
