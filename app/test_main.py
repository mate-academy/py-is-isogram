import pytest


from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word, result",
        [
            pytest.param(
                "",
                True,
                id="void string"
            ),
            pytest.param(
                "dragon",
                True,
                id="isogram word"
            ),
            pytest.param(
                "Adam",
                False,
                id="not isogram word"
            ),
            pytest.param(
                "look",
                False,
                id="not isogram word"
            )
        ]
    )
    def test_is_isogram(
            self,
            word: str,
            result: bool
    ) -> None:
        assert is_isogram(word) == result
