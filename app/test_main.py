import pytest

from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word, result",
        [
            pytest.param("", True,
                         id="should_return_True_for_empty_string"),
            pytest.param("playgrounds", True,
                         id="should_return_True_if_no_repeats"),
            pytest.param("look", False,
                         id="should_return_False_if_two_equal_letters"),
            pytest.param("Adam", False,
                         id="should_return_False_if_"
                            + "two_equal_letters_but_different_case"),
            pytest.param("loook", False,
                         id="should_return_False_if_three_equal_letters"),
        ]
    )
    def test_returns_correct_result(self, word: str, result: str) -> None:
        assert is_isogram(word) == result
