import pytest
from app import main


@pytest.mark.parametrize(
    "word, expected",
    [
        ("", True),
        ("a", True),
        ("A", True),
        ("abcdef", True),
        ("word", True),
        ("playgrounds", True),
        ("Word", True),

        ("aa", False),
        ("zZ", False),
        ("Adam", False),
        ("hello", False),
        ("ball", False),
        ("look", False),
        ("aabbcc", False),
        ("Alphabet", False),
    ],
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert main.is_isogram(word) is expected
