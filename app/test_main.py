from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word, expected",
    [
        ("word", True),
        ("second", True),
        ("amalgama", False),
        ("", True),
        ("abcdefghj", True),
        ("AaBb", False),
        ("Bob", False)
    ]
)
def test_is_isogram(word: str , expected: bool) -> None:

    assert is_isogram(word) == expected
