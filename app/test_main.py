from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "input_str,expected_bool",
    [
        pytest.param(
            "playgrounds",
            True
        ),
        pytest.param(
            "look",
            False
        ),
        pytest.param(
            "Adam",
            False
        ),
        pytest.param(
            "",
            True
        )
    ]
)
def test_audit_isogram(input_str: str, expected_bool: bool) -> None:
    assert is_isogram(input_str) == expected_bool
