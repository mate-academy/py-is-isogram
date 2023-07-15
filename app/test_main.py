import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected_value",
    [
        ("", True),
        ("Playgrounds", True),
        ("Adam", False),
        ("look", False)
    ],
    ids=[
        "Empty string is isogram",
        "Case insensitivity and non-repeating letters are isogram",
        "Repetition of the same lower and uppercase letter is not an isogram",
        "Adjacent repeated letters are not isogram"
    ]

)
def test_word_check_for_repeated_letters(
        word: str,
        expected_value: bool
) -> None:
    assert is_isogram(word) == expected_value
