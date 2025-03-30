import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "test_isogram, expected",
    [
        ("playground", True),
        ("Adam", False),
        ("", True),
        ("Python", True),
    ]
)
def test_for_isogram(test_isogram: str, expected: bool) -> None:
    assert is_isogram(test_isogram) == expected
