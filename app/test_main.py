import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        pytest.param("", True, id="empty_string_is_isogram"),
        pytest.param("isogram", True, id="lowercase_isogram"),
        pytest.param("alphabet", False, id="lowercase_not_isogram"),

        pytest.param("Aa", False, id="case_insensitive_repetition"),
        pytest.param("Look", False, id="consecutive_letters_repetition"),
        pytest.param("Andrew", True, id="isogram_with_capital_letter"),

        pytest.param("thumbscrewjapingly", True, id="long_isogram"),
        pytest.param("aba", False, id="first_and_last_letter_repetition"),
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) is expected
