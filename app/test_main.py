from app.main import is_isogram
import pytest


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word,result",
        [
            pytest.param(
              "playgrounds",
                True,
                id="Test function for word without repeating letter"
            ),
            pytest.param(
                "look",
                False,
                id="Test function for word with repeating letter"
            ),
            pytest.param(
                "Adam",
                False,
                id="Test function for word with repeating upper letter"
            ),
            pytest.param(
                "",
                True,
                id="Test function without word"
            ),
            pytest.param(
                "123",
                True,
                id="Test function with string number"
            ),
        ]
    )
    def test_is_isogram(
            self,
            word: str,
            result: bool
        ) -> None:
        assert is_isogram(word) == result

    @pytest.mark.parametrize(
        "word, error",
        [
            pytest.param(
                12,
                AttributeError,
                id="word should be string, not int!"
            ),
            pytest.param(
                ["123"],
                AttributeError,
                id="word should be string, not list!"
            ),
        ]
    )
    def test_function_value(
            self,
            word: str,
            error: TypeError
    ):
        with pytest.raises(error):
            is_isogram(word)
