import pytest
from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word, bool_result",
        [
            pytest.param(
                "",
                True,
                id="Function 'is_isogram' should return True for ''"
            ),
            pytest.param(
                "Adam",
                False,
                id="Function 'is_isogram' should return False for 'Adam'"
            ),
            pytest.param(
                "playgrounds",
                True,
                id="Function 'is_isogram' should return True for 'playgrounds'"
            ),
            pytest.param(
                "look",
                False,
                id="Function 'is_isogram' should return False for 'look'"
            )
        ]
    )
    def test_is_isogram(self, word: str, bool_result: bool) -> None:
        assert is_isogram(word) == bool_result
