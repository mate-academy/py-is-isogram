import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "initial, expected",
    [
        pytest.param(
            "", True,
            id="return True because empty string is isogram",
        ),
        pytest.param(
            "background", True,
            id="return True because background is isogram",
        ),
        pytest.param(
            "Memory", False,
            id="return False because function is case-insensitive",
        ),
        pytest.param(
            "abcab", False,
            id="return False because abcab in not isogram"
        ),
        pytest.param(
            "look", False,
            id="return False because look in not isogram",
        ),
        pytest.param(
            "radar", False,
            id="return False because radar in not isogram",
        )
    ]
)
def test_return_is_isogram(initial: str, expected: bool) -> None:
    assert is_isogram(initial) == expected