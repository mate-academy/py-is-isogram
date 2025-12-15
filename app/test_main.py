import pytest
import string
from typing import Any
from app.main import is_isogram


class TestIsIsogramValidInput:

    # Basic Positive Cases (True isograms)
    @pytest.mark.parametrize(
        "word, expected",
        [
            ("playgrounds", True),
            ("abcdefghijklmnopqrstuvwxyz", True),
            ("a", True),
            ("Z", True),
            ("Background", True),
            ("Python", True),
        ],
        ids=[
            "simple_isogram",
            "entire_alphabet",
            "single_lowercase",
            "single_uppercase",
            "mixed_case_unique",
            "python_unique",
        ]
    )
    def test_true_isograms(self, word: str, expected: bool) -> None:
        assert is_isogram(word) is expected

    # Basic Negative Cases (Non-isograms)
    @pytest.mark.parametrize(
        "word, expected",
        [
            ("look", False),
            ("Adam", False),
            ("eleven", False),
            ("mississippi", False),
            ("HELLO", False),
            ("HeLlO", False),
            ("Java", False),
            ("Aa", False),
            ("bB", False),
            ("AbCdEfGa", False),
        ],
        ids=[
            "consecutive_repeat",
            "case_insensitive_adam",
            "non_consecutive",
            "multiple_repeats",
            "uppercase_repeat",
            "mixed_case_repeat",
            "java_case_insensitive",
            "same_letter_different_cases_1",
            "same_letter_different_cases_2",
            "mixed_case_repeat_ends",
        ]
    )
    def test_false_isograms(self, word: str, expected: bool) -> None:
        assert is_isogram(word) is expected

    # Edge Cases
    def test_empty_string(self) -> None:
        assert is_isogram("") is True

    # Boundary/Long String Tests
    def test_boundary_cases(self) -> None:
        assert is_isogram("a" * 100) is False

    def test_long_unique_string(self) -> None:
        long_unique = string.ascii_lowercase + string.ascii_uppercase
        assert is_isogram(long_unique) is False


class TestIsIsogramInvalidInput:
    # TypeError Tests
    @pytest.mark.parametrize(
        "invalid_input",
        [
            123,
            3.14,
            None,
            ["hello"],
            {"word": "test"},
            True,
            False,
        ],
        ids=[
            "integer",
            "float",
            "none",
            "list",
            "dict",
            "boolean_true",
            "boolean_false",
        ]
    )
    def test_type_error_cases(self, invalid_input: Any) -> None:
        with pytest.raises(AttributeError):
            is_isogram(invalid_input)
