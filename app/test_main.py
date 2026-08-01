import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "string, result",
    [
        ("", True),
        ("Aa", False),
        ("a", True),
        ("sas", False)
    ]
)
def test_is_isogram(string: str, result: bool) -> None:
    assert is_isogram(string) == result
