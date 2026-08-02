import pytest

from app.main import is_isogram


class TestWordIsIsogram:
    @pytest.mark.parametrize(
        "word,expected_result",
        [
            ("", True),
            ("playgrounds", True),
            ("look", False),
            ("People", False),

        ],
        ids=[
            'Should return True if the word is an empty string: ""',
            "Should return True if there are no repeated letters in the word",
            "Should return False if there are two or "
            "more repeated letters in the word",
            "Should return False if there are two repeated "
            "letters in the word, regardless of case",
        ]
    )
    def test_should_correct_bool_values_when_word_is_string(
            self,
            word: str,
            expected_result: bool
    ) -> None:
        assert is_isogram(word) == expected_result

    def test_should_cause_an_error_if_the_word_is_not_a_string(self) -> None:
        with pytest.raises(AttributeError):
            is_isogram(345)
