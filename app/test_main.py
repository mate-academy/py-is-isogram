from app.main import is_isogram
import pytest


class TestIsogram:

    @pytest.mark.parametrize(
        "word,result",
        [
            ("playgrounds", True),
            ("Sasuke", False),
            ("mackbook", False),
            ("", True)
        ]
    )
    def test_isogram_is_correct(
            self,
            word: str,
            result: bool
    ) -> None:

        assert is_isogram(word) == result

    @pytest.mark.parametrize(
        "word,expected_error",
        [
            pytest.param(
                "Zhan Peck", ValueError,
                id="should not be spaces in word"
            ),
            pytest.param(
                ["Ivanko"], AttributeError,
                id="Taking word should be string"
            )
        ]
    )
    def test_raising_error_correctly(
            self,
            word: str,
            expected_error: type[Exception]
    ) -> None:

        with pytest.raises(expected_error):
            is_isogram(word)
