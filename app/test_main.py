import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("", True),
        ("a", True),
        ("isogram", True),
        ("hello", False),
        ("Test", False),
        ("python", True),
        ("AaBbCc", False),
        ("abcdABCD", False),
        ("reappear", False),
        ("moose", False),
        ("Apple", False),
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
