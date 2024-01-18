import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
    ],
    ids=[
        "playgrounds is isogram",
        "not only non-consecutive letters are not an isogram",
        "string with different cases of the same letter is not an isogram",
        "empty string is an isogram"
    ]
)
def test_is_isogram(test_input: str, expected: bool) -> None:
    assert is_isogram(test_input) == expected
