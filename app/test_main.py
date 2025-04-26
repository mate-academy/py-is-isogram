import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "st, res",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True)
    ],
    ids=[
        "all unique letters",
        "repeating letters",
        "case sensitive check",
        "empty string is isogram"
    ]
)
def test_is_isogram(st: str, res: bool) -> None:
    assert is_isogram(st) == res
