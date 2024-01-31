import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected_result",
    [
        ("playgrounds", True),
        ("kittens", False),
        ("madam", False),
        ("", True),
        ("kiTty", False),
    ],
    ids=[
        "should return True when word is an isogram",
        "should return False when the same letters are consecutive",
        "should return False when the same letters are in the word",
        "should return True when the string is empty",
        "should be case insensitive"
    ]
)
def test_is_isogram(
        word: str,
        expected_result: bool
) -> None:
    result = is_isogram(word)
    assert result == expected_result
