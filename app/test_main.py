import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("", True),
        ("playgrounds", True),
        ("look", False),
        ("Mom", False)
    ]
)
def test_isogram(word: str, expected: bool) -> None:
    assert (is_isogram(word) == expected), \
        f"for word '{word}' result should be {expected}"
