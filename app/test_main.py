import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "string,result",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True)
    ]
)
def test_is_isogram(
        string: str,
        result: bool
) -> None:
    assert is_isogram(string) is result
