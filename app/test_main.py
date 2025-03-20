from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word, expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("Library", False),
        ("1234", True),
        ("EXIT", True),
    ]
)
def test_value(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
