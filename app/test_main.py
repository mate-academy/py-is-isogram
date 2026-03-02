import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("", True),
        ("a", True),
        ("look", False),
        ("Adam", False),
        ("playgrounds", True)
    ],
    ids=[
        "empty",
        "one_letter",
        "two_repeated_letters",
        "repeated_upper_letters",
        "no_repeated_letters"]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
