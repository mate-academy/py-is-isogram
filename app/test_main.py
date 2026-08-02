import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected_result",
    [
        # Boundary conditions: порожній рядок та 1 символ
        pytest.param("", True, id="empty_string_is_isogram"),
        pytest.param("a", True, id="single_lowercase_letter"),
        pytest.param("Z", True, id="single_uppercase_letter"),

        pytest.param("playgrounds", True, id="valid_lowercase_isogram"),
        pytest.param("background", True, id="valid_another_isogram"),

        pytest.param("look", False, id="consecutive_repeated_letters"),

        pytest.param("aba", False, id="non_consecutive_repeated_letters"),

        pytest.param("Adam", False,
                     id="case_insensitive_same_letter_different_cases"),
        pytest.param("Moose", False, id="case_insensitive_mixed_case_repeat"),
    ]
)
def test_is_isogram(word: str, expected_result: bool) -> None:
    assert is_isogram(word) == expected_result
