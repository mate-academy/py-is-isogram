import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "isogram, expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True)
    ]
)
def test_is_isogram(isogram: str, expected: bool) -> None:
    assert is_isogram(isogram) == expected
