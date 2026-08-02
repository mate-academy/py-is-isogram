import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "string, expected",
    [

        ("", True),
        ("1", True),
        ("11", False),
        ("Analogy", False),
        ("#%*@)_#", False),
        ("python", True),
        ("  ", False),
    ],
    ids=[
        "empty_string_false",
        "one_char_True",
        "two_same_chars_False",
        "upper_letter_equal_to_lower_false",
        "2_repeated_symbols_false",
        "without_repeat_true",
        "2_spaces_false",
    ]
)
def test_is_isogram(string: str, expected: list) -> None:
    assert is_isogram(string) == expected, (
        f"Function 'is_isogram' should return {expected} "
        f"when string is {string}"
    )
