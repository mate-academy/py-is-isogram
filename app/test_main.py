import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected_isogram",
    [
        ("", True),
        ("look", False),
        ("playgrounds", True),
        ("Adam", False),
        ("Alex", True)
    ]
)
def test_is_isogram(word: str, expected_isogram: bool) -> None:
    assert is_isogram(word) == expected_isogram
