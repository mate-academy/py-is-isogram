from app.main import is_isogram

import pytest


class TestisIsogram:
    @pytest.mark.parametrize(
        "str_value, result",
        [
            pytest.param(
                "playgrounds", True, id="True for playgrounds"
            ),
            pytest.param(
                "look", False, id="False for look"
            ),
            pytest.param(
                "Adam",
                False, id="False for Adam"
            ),
            pytest.param(
                "",
                True, id="false for empty string"
            )
        ]
    )
    def test_is_isogram(
            self,
            str_value: str,
            result: bool) -> None:
        assert is_isogram(str_value) == result
