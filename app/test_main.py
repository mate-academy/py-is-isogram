from pytest import mark

from app.main import is_isogram


class TestIsIsogram:
    @mark.parametrize(
        "input_word, expected_result",
        [
            ("", True),
            ("Adam", False),
            ("look", False),
            ("playgrounds", True)
        ]
    )
    def test_check_if_word_is_isogram_correctly(
            self,
            input_word: str,
            expected_result: bool
    ) -> None:
        assert is_isogram(input_word) == expected_result
