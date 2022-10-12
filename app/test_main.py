import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "string_for_check,result",
    [
        pytest.param(
            "",
            True,
            id="empty string"
        ),
        pytest.param(
            "look",
            False,
            id="repeating letters in string"
        ),
        pytest.param(
            "Adam",
            False,
            id="repeating letters are not the same case in string"
        ),
        pytest.param(
            "playgrounds",
            True,
            id="no repeating letters in string"
        ),
    ]
)
def test_return_correct_result(string_for_check: str, result: bool):
    assert is_isogram(string_for_check) == result
