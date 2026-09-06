import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "text,expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True)
    ]
)
def test_is_isogram(text: str, expected: bool) -> None:
    assert is_isogram(text) == expected
