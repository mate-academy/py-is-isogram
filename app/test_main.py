import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "str_value, expected",
    [
        pytest.param(
            "",
            True,
            id="Function should work correct with empty string"
        ),

        pytest.param(
            "playgrounds",
            True,
            id="Function should work correct with string without duplicates"
        ),

        pytest.param(
            "Adam",
            False,
            id="Function shouldn't work correct with string which\
             has duplicates of with different registers!"
        ),

        pytest.param(
            "look",
            False,
            id="Function shouldn't work correct with string which\
             has duplicates!"
        )
    ])
def test_is_isogram(
        str_value: str,
        expected: bool
) -> None:
    assert is_isogram(str_value) == expected
