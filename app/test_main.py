import pytest
from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "input_world, expested",
        [
            pytest.param(
                "", True,
                id="the empty string is an isogram"
            ),
            pytest.param(
                "Python", True,
                id="should be case-insensitive"
            ),
            pytest.param(
                "adam", False,
                id="not consecutive letters are not an isogram"
            ),
            pytest.param(
                "loOk", False,
                id="register of the letter does not matter"
            ),
        ]
    )
    def test_is_isogran(self, input_world: str,
                        expested: str) -> None:
        assert is_isogram(input_world) == expested
