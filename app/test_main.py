import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected",
    [
        ("", True),
        ("TrUe", True),
        ("lOok", False),
        ("Adam", False),
    ], ids=[
        "empty string should be True",
        "should be true if contains upper not repeated letters",
        "should be false if contains the same consecutive letters",
        "should be false if contains the same non-consecutive letters"
    ]
)
def test_should_return_proper_isogram_check(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
