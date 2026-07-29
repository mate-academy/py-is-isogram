import pytest

from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word,expected_result",
        [
            pytest.param("", True),
            pytest.param("playgrounds", True),
            pytest.param("look", False),
            pytest.param("package", False),
            pytest.param("Adam", False),
        ],
        ids=[
            "empty_string_is_isogram",
            "word_with_unique_letters_is_isogram",
            "word_with_repeated_letters_is_not_isogram",
            "word_with_non_consecutive_repeated_letters_is_not_isogram",
            "isogram_check_is_case_insensitive"
        ]
    )
    def test_is_isogram(self, word: str, expected_result: bool) -> None:
        assert is_isogram(word) == expected_result
