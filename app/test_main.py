import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected_result",
    [
        ("isogram", True),
        ("", True),
        ("hello", False),
        ("abcABC", False),
        ("a", True),
        ("aa", False),
        ("123", True),
        ("ab1c1", False),
    ],
    ids=[
        "simple isogram",
        "empty string",
        "repeated 'l' in hello",
        "same letters in different cases",

        "single letter",
        "two identical letters",
        "digits should be allowed",
        "word with repeated digit",
    ]
)
def test_is_isogram(word: str, expected_result: bool) -> None:
    assert is_isogram(word) == expected_result
