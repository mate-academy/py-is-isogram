from app.main import is_isogram

import pytest


@pytest.mark.parametrize(
    "word, expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
    ],
    ids=[
        "word 'playgrounds'",
        "word 'look'",
        "word 'Adam'",
        "empty string",
    ]
)
def test_check_if_word_is_isogram(word: str, expected: bool) -> None:
    assert (
        is_isogram(word) == expected
    ), f"Isogram check for {word} should be {expected}"
