import pytest

from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word, result",
        [
            ("Playgrounds", True),
            ("playgrounds", True),
            ("look", False),
            ("Adam", False),
            ("", True),
        ],
        ids=[
            "should be case-insensitive for 'Playgrounds'",
            "should return correct value for 'playgrounds'",
            "should return correct value for 'look'",
            "should return correct value for 'Adam'",
            "should return correct value for empty string"
        ]
    )
    def test_checks_isogram_correctly(
            self, word: str, result: bool
    ) -> None:

        assert is_isogram(word) == result

    @pytest.mark.parametrize(
        "word, expected_error",
        [
            (1, AttributeError),
            ([], AttributeError)
        ],
        ids=[
            "should raise an error if parameters is integer",
            "should raise an error if parameters is list"
        ]
    )
    def test_should_raise_a_correct_error(
            self, word: str, expected_error: Exception
    ) -> None:

        with pytest.raises(expected_error):
            is_isogram(word)
