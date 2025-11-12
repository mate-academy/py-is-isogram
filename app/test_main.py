import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected_result",
    [
        ("playgrounds", True),
        ("Dermatoglyphics", True),
        ("", True),
        ("a", True),
        ("look", False),
        ("Adam", False),
        ("Aa", False),
    ],
    ids=[
        "no_repeats",
        "long_word",
        "empty_string",
        "one_string",
        "repeated_letters",
        "problem_with_register",
        "register_check"
    ]

)
def test_is_isogram_all_cases(word: str, expected_result: bool) -> None:
    assert is_isogram(word) is expected_result
