import pytest

from app.main import is_isogram


class TestIsIsogram:

    @pytest.mark.parametrize(
        "word,expected_answer",
        [
            ("", True),
            (" ", True),
            ("  ", False),
            ("moon", False),
            ("Ala", False),
            ("kajh/ndvyw$5#", True),
            ("playgrounds", True)
        ]
    )
    def test_is_isogram_expected_answer(
            self,
            word: str,
            expected_answer: bool
    ) -> None:
        assert is_isogram(word) == expected_answer

    @pytest.mark.parametrize(
        "word,expected_error",
        [
            (5, AttributeError),
            ({1}, AttributeError)
        ]
    )
    def test_raising_test_correctly(
            self,
            word: str,
            expected_error: [Exception]
    ) -> None:
        with pytest.raises(expected_error):
            is_isogram(word)
