import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "string,expected",
    [
        pytest.param(
            "",
            True,
            id="Should return true if string is empty"
        ),
        pytest.param(
            "Palp",
            False,
            id="Should return false with repeated uppercase and lowercase"
        ),
        pytest.param(
            "marked",
            True,
            id="Should return true if string is isogram"
        ),
        pytest.param(
            "look",
            False,
            id="Should return false if there are repeated letters"
        )
    ]
)
def test_is_isogram_function(
        string: str,
        expected: bool
) -> None:
    result = is_isogram(string)

    assert result == expected
