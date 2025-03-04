import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "string, result",
    [
        pytest.param(
            "",
            True,
            id="test should return true "
               "if string is empty"
        ),
        pytest.param(
            "qwertyuiopasdfghjklzxcvbnm",
            True,
            id="test should work correctly with "
               "string that contains all letters"
        ),
        pytest.param(
            "Babo",
            False,
            id="test should return false due to case insensitive function"
        ),
        pytest.param(
            "A",
            True,
            id="test should return true if string contains 1 letter"
        ),
        pytest.param(
            "playgrounds",
            True,
            id="test should return true if string is isogram"
        ),
        pytest.param(
            "abca",
            False,
            id="test should return false if letters repeat non-consecutively"
        )
    ]
)
def test_should_return_correct_bool_value(
        string: str,
        result: bool
) -> None:
    assert is_isogram(string) == result
