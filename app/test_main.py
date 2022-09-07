import pytest

from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word, value",
        [
            pytest.param(
                "playgrounds",
                True,
                id="all chars are different"
            ),
            pytest.param(
                "look",
                False,
                id="the more than one char"

            ),
            pytest.param(
               "Adam",
                False,
                id="the more than one char: upper and lower"
            ),
            pytest.param(
                "",
                True,
                id="empty is isogram"
            )
        ]
    )
    def test_should_correctly_values(
            self,
            word,
            value
    ):
        assert is_isogram(word) == value
