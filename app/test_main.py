from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word, expected_boolean",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("a", True)
    ]
)
def test_is_isogram(word: str, expected_boolean: bool) -> None:
    assert is_isogram(word) == expected_boolean
