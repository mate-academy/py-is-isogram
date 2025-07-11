import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "input_str, expected",
    [
        pytest.param(
            "",
            True,
            id="test when string is empty"
        ),
        pytest.param(
            "background",
            True,
            id="test when letters don't repeat"
        ),
        pytest.param(
            "book",
            False,
            id="test when letters repeat"
        ),
        pytest.param(
            "Test",
            False,
            id="test when letters in different case are repeated"
        )
    ]
)
def test_is_isogram(input_str: str, expected: bool) -> None:
    assert is_isogram(input_str) == expected
