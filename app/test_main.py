import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "string,expected_result",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True)
    ]
)
def test_is_isogram(string: str,
                    expected_result: bool) -> None:
    assert is_isogram(string) == expected_result
