import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("playgrounds", True),   # no repeats at all
        ("", True),              # empty string counts as isogram
        ("a", True),             # single letter
        ("PLAYGROUNDS", True),   # uppercase isogram
        ("look", False),         # consecutive repeat
        ("abca", False),         # non-consecutive repeat
        ("Adam", False),         # repeat in different case
        ("aaaa", False),         # all letters the same
    ],
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) is expected
