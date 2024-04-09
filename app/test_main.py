import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expect_word",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True)
    ],
    ids=[
        "word that has no repeating letters",
        "repeating letters in word",
        "A and a are considered the same letter",
        "the empty string is an isogram"
    ]
)
def test_verify_all_letters_in_word(word: str, expect_word: bool) -> None:
    assert (is_isogram(word) == expect_word), \
        f"The given word: {word} must be an inogram"
