import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "string,expected_value",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
    ],
    ids=[
        "Playgrounds should be isogram",
        "look should not be isogram",
        "Adam should not be isogram",
        "Empty string should be isogram",
    ]
)
def test_is_isogram(string: str, expected_value: bool) -> None:
    assert is_isogram(string) == expected_value
