import pytest
from app.main import is_isogram


class TestShouldWorkCorrectly:
    @pytest.mark.parametrize(
        "initial_word,expected_word",
        [
            ("playgrounds", True),
            ("racoon", False),
            ("Madam", False),
            ("", True),
            ("Berlin", True)
        ],
        ids=[
            "This word is an isogram.",
            "Not only consecutive letters are not an isogram.",
            "Not only non-consecutive letters are not an isogram.",
            "Empty string is an isogram.",
            "This word is an isogram."
        ]
    )
    def test_should_find_an_isogram(
            self,
            initial_word: str,
            expected_word: str
    ) -> None:
        assert is_isogram(initial_word) == expected_word

    @pytest.mark.parametrize(
        "initial_word,expected_error",
        [
            (1, AttributeError),
            ((1, "apple"), AttributeError)
        ],
        ids=[
            "Should raise error if word is not a string!",
            "Should raise error if word is a tuple!"
        ]
    )
    def test_should_raise_error_if_word_is_not_a_string(
            self,
            initial_word: str,
            expected_error: Exception
    ) -> None:
        with pytest.raises(expected_error):
            is_isogram(initial_word)
