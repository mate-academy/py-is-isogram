import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ('playgrounds', True),
        ('look', False),
        ('Adam', False),
        ('', True),

        ('isogram', True),
        ('background', True),
        ('hello', False),
        ('Jambox', True),
        ('Moose', False),
        ('aBcDeFgA', False),
        ('zyxw', True),
    ],
    ids=[
        "example_playgrounds_true",
        "example_look_false",
        "example_adam_false_case_insensitive",
        "example_empty_string_true",
        "basic_isogram",
        "long_isogram",
        "common_repeat",
        "case_check_true",
        "case_check_false_with_repeat",
        "case_insensitive_false",
        "short_isogram",
    ]
)
def test_is_isogram_valid_words(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
