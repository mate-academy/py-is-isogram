import pytest
from app.main import is_isogram


class TestIsIsogramFuncClass:
    @pytest.mark.parametrize(
        "word,expected_answer",
        [
            pytest.param(
                "playgrounds",
                True,
                id="Word=playgrounds, answer=True"
            ),
            pytest.param(
                "look",
                False,
                id="Word=look, answer=False"
            ),
            pytest.param(
                "Adam",
                False,
                id="Word=Adam, answer=False"
            ),
            pytest.param(
                "",
                True,
                id="Word='', answer=True"
            )
        ]
    )
    def test_is_isogram(
            self,
            word: str,
            expected_answer: bool
    ) -> None:
        assert is_isogram(word) == expected_answer
