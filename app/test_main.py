from app.main import is_isogram
import pytest


class TestIsogramFunction:
    @pytest.mark.parametrize(
        "word,result",
        [
            pytest.param(
                "playgrounds",
                True,
                id="word playgrounds should return True"
            ),
            pytest.param(
                "look",
                False,
                id="word look should return False"
            ),
            pytest.param(
                "Adam",
                False,
                id="word Adam should return False"
            ),
            pytest.param(
                "",
                True,
                id="empty should return True"
            )
        ]
    )
    def test_is_isogram_function_working_correct(self,
                                                 word: str,
                                                 result: bool) -> None:
        assert is_isogram(word) == result
