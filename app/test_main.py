import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "string, expected",
    [
        ("", True),
        ("1", True),
        ("11", False),
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
    ]
)
def test_main(string: str, expected: bool) -> None:
    assert is_isogram(string) == expected
