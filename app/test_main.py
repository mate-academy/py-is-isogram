import pytest
from app.main import is_isogram


class TestIsIsogram():
    @pytest.mark.parametrize(
        "word,result",
        [
            pytest.param(
                "playgrounds",
                True,
                id="check different letter"
            ),
            pytest.param(
                "look",
                False,
                id="check double letter"
            ),
            pytest.param(
                "Adam",
                False,
                id="check with high letter"
            ),
            pytest.param(
                "",
                True,
                id="check empty word"
            ),
        ]
    )
    def test_is_isogram(
            self,
            word: str,
            result: bool
    ) -> None:
        assert is_isogram(word) is result
