import pytest

from app.main import is_isogram


class TestIsogramFunction:
    @pytest.mark.parametrize(
        "word,result",
        [
            (
                "playgrounds",
                True
            ),
            (
                "look",
                False
            ),
            (
                "Adam",
                False
            ),
            (
                "",
                True
            ),
            (
                "1a1",
                False
            )
        ]
    )
    def test_isogram_function_returns_correct_response(
            self,
            word: str,
            result: bool
    ) -> None:

        assert is_isogram(word) == result

    @pytest.mark.parametrize(
        "word,error",
        [
            (
                1,
                AttributeError
            )
        ]
    )
    def test_expected_errors(
            self,
            word: any,
            error: AttributeError
    ) -> None:
        with pytest.raises(error):
            is_isogram(word)
