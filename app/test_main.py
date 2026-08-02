import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "input_string,bool_value",
    [
        pytest.param(
            "ground", True, id="check_when_word_is_isogram"
        ),
        pytest.param(
            "Playground", True, id="check_word_contain_upper_letter"
        ),
        pytest.param(
            "", True, id="check_input_string_is_empty"
        ),
        pytest.param(
            "look", False, id="check_when_word_contain_two_consecutive_letter"
        ),
        pytest.param(
            "Adam", False, id="check_two_same_letter"
        )
    ]
)
def test_is_isogram(input_string: str, bool_value: bool) -> None:
    assert is_isogram(input_string) is bool_value
