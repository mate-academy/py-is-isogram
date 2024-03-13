import traceback

import pytest
from app.main import is_isogram


class TestIsogramParam:
    @pytest.mark.parametrize(
        "word,expected",
        [
            pytest.param(
                "",
                True,
                id="test empty isogram"
            ),
            pytest.param(
                "insensitive",
                False,
                id="test non consecutive not isogram"
            ),
            pytest.param(
                "lOok",
                False,
                id="test diff cases"
            ),
            pytest.param(
                "aaaaaaaaaaaaaaaaahhhhhhhhhhh",
                False,
                id="test many letters"
            )
        ]
    )

    def test_correct_return(self, word: str, expected: bool) -> None:
        assert is_isogram(word) is expected
