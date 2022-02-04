import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "string, expected_value",
    [
        pytest.param(
            'playgrounds',
            True,
            id="test is isogram"
        ),
        pytest.param(
            'look',
            False,
            id="test is not isogram"),
        pytest.param(
            'Adam',
            False,
            id="test is not isogram with different case"
        ),
        pytest.param(
            '',
            True,
            id="test empty string is isogram"
        )
    ]
)
def test_is_isogram(string, expected_value):
    assert is_isogram(string) == expected_value

