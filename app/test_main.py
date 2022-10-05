import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "isogram,expected_result",
    [
        pytest.param(
            "", True,
            id="empty string"
        ),
        pytest.param(
            "playgrounds", True,
            id="valid string"
        ),
        pytest.param(
            "abcdefghijklmnopqrstuvwxyz", True,
            id="string with alphabet"
        ),
        pytest.param(
            "adrian", False,
            id="with two identical letters"
        ),
        pytest.param(
            "sss", False,
            id="string with identical letters"
        ),
        pytest.param(
            "Adrian", False,
            id="string with uppercase"
        ),
        pytest.param(
            "a", True,
            id="string with one letter lowercase"
        ),
        pytest.param(
            "A", True,
            id="string with one letter uppercase"
        ),
    ]
)
def test_is_isogram(isogram: str, expected_result: bool) -> None:
    assert is_isogram(isogram) == expected_result
