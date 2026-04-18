import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, check_is_isogram",
    [
        ("loOk", False),
        ("apple", False),
        ("Pp", False),
        ("Mama", False),
        ("", True),
        ("Mate", True),
        ("a", True)
    ]
)
def test_word_is_isogram_with_true_and_false_values(
        word: str,
        check_is_isogram: bool
) -> None:
    assert is_isogram(word) == check_is_isogram, \
        f"Result of check of {word} should be {not is_isogram(word)}"
