import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("", True),
        ("table", True),
        ("book", False),
        ("bOok", False),
        ("return", False),
    ],
    ids=[
        "should return True for empty string",
        "should return True for isogram with lowercase letters",
        "should return False for non isogram with lowercase letters",
        "should return False for non isogram "
        + "if repeated letters in both upper and lower case",
        "should return False for non isogram "
        + "if repeated letters are not consecutive"
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
