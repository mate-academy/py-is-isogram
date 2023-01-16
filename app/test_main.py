from app.main import is_isogram
import pytest


class TestIsIsogram:
    @pytest.mark.parametrize(
        "value, answer",
        [
            pytest.param(
                "HeLlo", False,
                id="test value = 0"
            ),
            pytest.param(
                "isogram", True,
                id="test add 1 penny"
            ),
            pytest.param(
                "IsiSoGrAgM", False,
                id="test add 1 nickel "
            ),
            pytest.param(
                "", True,
                id="test add 1 nickel "),
            pytest.param(
                "loose", False,
                id="test add 1 nickel ")
        ]
    )
    def test_get_coin(self, value, answer):
        assert is_isogram(value) == answer
