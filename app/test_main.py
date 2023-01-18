import pytest

from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word,expected_result",
        [
            pytest.param(
                "playgrounds",
                True,
                id="'playgrounds' is True"
            ),
            pytest.param(
                "look",
                False,
                id="'look' is False"
            ),
            pytest.param(
                "Adam",
                False,
                id="'Adam' is False"
            ),
            pytest.param(
                "",
                True,
                id="Empty string is True"
            ),
        ]
    )
    def test_is_isogram(
            self,
            word: str,
            expected_result: bool
    ) -> None:
        assert is_isogram(word) == expected_result
