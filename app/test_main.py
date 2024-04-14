from app.main import is_isogram


import pytest


class TestFunc:
    @pytest.mark.parametrize(
        "word,result",
        [
            pytest.param(
                "Ada",
                False,
                id="test case sensitive"
            ),
            pytest.param(
                "",
                True,
                id="test empty string is OK"
            ),
            pytest.param(
                "AbCdEfG",
                True,
                id="test isogram"
            )
        ]
    )
    def test1(self, word: str, result: bool) -> None:
        assert is_isogram(word) is result
