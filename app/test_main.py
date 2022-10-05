import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "isogram,expected",
    [
        pytest.param(
            "playgrounds", True,
            id="check valid string"
        ),
        pytest.param(
            "abcdefghijklmnopqrstuvwxyz", True,
            id="check string with alphabet"
        ),
        pytest.param(
            "look", False,
            id="check string with two identical letters"
        ),
        pytest.param(
            "HHHhhhhhH", False,
            id="check string with identical letters"
        ),
        pytest.param(
            "Adam", False,
            id="check string with uppercase"
        ),
        pytest.param(
            "", True,
            id="check empty string"
        ),
        pytest.param(
            "a", True,
            id="check string with one letter"
        ),
    ]
)
def test_is_isogram(isogram: str, expected: bool) -> None:
    assert is_isogram(isogram) == expected
