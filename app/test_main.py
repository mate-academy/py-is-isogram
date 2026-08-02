import pytest
from app.main import is_isogram


# write your code here
@pytest.mark.parametrize(
    "input_word, expected_output",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True)
    ],
    ids=[
        "Must be isogram, because word has no repeating letters",
        "Mustn't be isogram, because word has repeating letters",
        "String with different cases of the same letter is not an isogram",
        "Empty string is an isogram"
    ]
)
def test_is_isogram(input_word: str, expected_output: bool) -> None:
    assert is_isogram(input_word) == expected_output
