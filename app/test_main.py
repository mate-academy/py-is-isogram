from app.main import is_isogram

import pytest


class TestIsIsogram:
    @pytest.mark.parametrize(
        "initial_sting,expected_result",
        [
            pytest.param(
                "",
                True,
                id="empty string is a isogram"
            ),
            pytest.param(
                "ADAM",
                False,
                id="should be case insensitive when sting is not isogram"
            ),
            (
                "hotel",
                True
            ),
            (
                "loOk",
                False
            ),
        ]
    )
    def test_should_return_correctly_value(
            self,
            initial_sting: str,
            expected_result: bool
    ) -> None:
        assert is_isogram(initial_sting) == expected_result
