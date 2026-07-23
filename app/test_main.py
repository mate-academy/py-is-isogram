import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "string, expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
    ]
)
def test_is_isogram_returns_expected_result(
        string: str,
        expected: bool
) -> None:
    assert is_isogram(string) == expected
