from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "_input, expected",
    [
        pytest.param(
            "playgrounds", True,
            id="For 'playgrounds' expected True"
        ),
        pytest.param(
            "", True,
            id="For '' expected True"
        ),
        pytest.param(
            "look", False,
            id="For 'look' expected False"
        ),
        pytest.param(
            "Adam", False,
            id="For 'Adam' expected False"
        )
    ],
)
def test_isogram(_input: str, expected: bool) -> None:
    assert is_isogram(_input) == expected
