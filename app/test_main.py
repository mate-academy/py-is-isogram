from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word,expected",
    [
        ("", True),
        ("Adam", False),
        ("playgrounds", True),
        ("hello", False),
    ],

    ids=[
        "get_empty_value_expected_True",
        "get_value_with_upper_letter_expected_False",
        "get_value_with_lower_letter_expected_True",
        "get_consecutive_repeats_value_expected_False",
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert (
        is_isogram(word) is expected
    ), f"With {word} argument expected {expected}"
