from app.main import is_isogram

import pytest


@pytest.mark.parametrize(
    "input_string, result",
    [
        pytest.param(
            "playgrounds",
            True,
            id="should return true when isogram"
        ),
        pytest.param(
            "adam",
            False,
            id="should return false when not isogram"
        ),
        pytest.param(
            "lOoK",
            False,
            id="should be case insensitive"
        ),
        pytest.param(
            "",
            True,
            id="empty string is an isogram"
        )
    ]
)
def test_checks_if_word_is_isogram_correctly(
        input_string: str,
        result: bool
) -> None:
    assert is_isogram(input_string) == result
