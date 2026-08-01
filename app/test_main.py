from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word, expected",
    [
        ("Playground", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("p", True),
        ("pp", False)
    ]
)
def test_validate_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
