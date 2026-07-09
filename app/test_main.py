from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "text,expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("", True),
        ("Adam", False),
        ("Test", False),

    ],
    ids=[]
)
def test_is_isogram(text: str, expected: bool) -> None:
    assert is_isogram(text) == expected
