import pytest

from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "input_word, is_iso",
        [
            pytest.param(
                "", True,
                id="empty_string_shoul_be_isogram"
            ),
            pytest.param(
                "MiLkCow", True,
                id="function_should_be_case_insensitive"
            ),
            pytest.param(
                "PatTern", False,
                id=("input_with_different_cases_of"
                    "_same_letter_should_not_be_an_isogram")
            ),
            pytest.param(
                "Noon", False,
                id="consecutive_repeating_letters_as_input_should_return_false"
            ),
            pytest.param(
                "Banana", False,
                id=("test_non_consecutive_repeating_letters"
                    "_as_input_should_return_false")
            ),
            pytest.param(
                "Abcdefghijklmnopqrstuvwxyz", True,
                id="function_with_no_repeating_letters_should_be_true"
            )
        ]
    )
    def test_is_isogram(
            self,
            input_word: str,
            is_iso: bool
    ) -> None:
        assert is_isogram(input_word) == is_iso
