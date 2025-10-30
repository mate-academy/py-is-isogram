import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "test_input, expected",
    [
        pytest.param(
            "",
            True,
            id="empty string",
        ),
        pytest.param(
            "look",
            False,
            id="not empty string False",
        ),
        pytest.param(
            "Adam",
            False,
            id="different cases of the letter is not an isogram",
        ),
        pytest.param(
            "playgrounds",
            True,
            id="Not only consecutive letters are not an isogram",
        )
    ]
)
def test_is_isogram(test_input: str, expected: bool) -> None:
    assert is_isogram(test_input) == expected
