from app.main import is_isogram
import pytest


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word, expected_result",
        [
            ("playgrounds", True),
            ("PlayGrounds", True),
            ("look", False),
            ("Adam", False),
            ("", True)
        ],
        ids=[
            "playgrounds should be returned True",
            "PlayGrounds should be returned True",
            "look should be returned True",
            "Adam should be returned True",
            "'' should be returned True"
        ]
    )
    def test_returning_is_isogram(
        self,
        word: str,
        expected_result: bool,
    ) -> None:
        assert is_isogram(word) == expected_result

    @pytest.mark.parametrize(
        "input_data, error",
        [
            (1, AttributeError),
            (True, AttributeError)
        ],
        ids=[
            "1 should be raised AttributeError",
            "True should be raised AttributeError"
        ]
    )
    def test_raising_errors_for_is_isogram(
        self,
        input_data: any,
        error: Exception
    ) -> None:
        with pytest.raises(error):
            is_isogram(input_data)
