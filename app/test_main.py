from app.main import is_isogram

import pytest


@pytest.mark.parametrize(
    "word, expected_result",
    [
        ("", True),
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("MaMa", False),
    ],
    ids=[
        "test_empty_word",
        "test_isogram_word",
        "test_word_in_lower_case",
        "test_word_with_uppercase_character",
        "test_word_with_repeating_syllable"
    ]
)
def test_is_isogram(word, expected_result):
    assert is_isogram(word) == expected_result
