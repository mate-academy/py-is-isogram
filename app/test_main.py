import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected_value",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True)
    ]
)
def test_is_isogram(word: str, expected_value: bool) -> None:
    assert is_isogram(word) is expected_value
