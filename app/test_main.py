from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word, bool_value",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("a a aaaa aaaa aa AAAA AAA AAA a AaAaA", False),
    ]
)
def test_is_isogram(word: str, bool_value: bool) -> None:
    assert is_isogram(word) == bool_value
