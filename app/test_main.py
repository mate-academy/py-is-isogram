import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "text,expected",
    [
        pytest.param(
            "",
            True,
            id="empty string"
        ),
        pytest.param(
            "MY my",
            False,
            id="non-empty string not isogram with CamelCase"
        ),
        pytest.param(
            "Sdfr",
            True,
            id="non-empty string isogram with CamelCase"
        ),
        pytest.param(
            "my best programming language with test isogram",
            False,
            id="non-empty long string not isogram"
        ),
        pytest.param(
            "oo",
            False,
            id="consecutive letters are not an isogram"
        )
    ]
)
def test_is_isogram(text: str, expected: bool) -> None:
    assert is_isogram(text) == expected
