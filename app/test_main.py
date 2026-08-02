import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "example, result",
    [
        ("", True),
        ("Adam", False),
        ("playgrounds", True),
        ("look", False)
    ],
    ids=[
        "test empty string",
        "test case-insensitivity",
        "test real isogram",
        "test not isogram"
    ]
)
def test_is_isogram(example: str, result: bool) -> None:
    assert is_isogram(example) is result
