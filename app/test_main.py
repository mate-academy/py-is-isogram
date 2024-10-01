from app.main import is_isogram


import pytest


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word,bool_result",
        [
            ("playgrounds", True),
            ("look", False),
            ("Adam", False),
            ("", True)
        ]
    )
    def test_is_isogram_correctly(
            self,
            word: any,
            bool_result: bool
    ) -> None:
        assert is_isogram(word) is bool_result

    @pytest.mark.parametrize(
        "word,expected_error",
        [
            (29, AttributeError),
            (None, AttributeError)
        ]
    )
    def test_raising_is_isogram(
            self,
            word: any,
            expected_error: Exception
    ) -> None:
        with pytest.raises(expected_error):
            is_isogram(word)
