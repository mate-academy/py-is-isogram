from app.main import is_isogram
import pytest


class TestIsIsogram:
    @pytest.mark.parametrize(
        "initial_data, expected_result",
        [
            pytest.param(
                "playgrounds",
                True,
                id="is isogram('playgrounds')"
            ),
            pytest.param(
                "look",
                False,
                id="is isogram('look')"
            ),
            pytest.param(
                "Adam",
                False,
                id="is isogram('Adam')"
            ),
            pytest.param(
                "",
                True,
                id="is isogram('')"
            ),

        ]
    )
    def test_app_checks_correctly(
            self,
            initial_data: str,
            expected_result: bool
    ) -> None:
        assert is_isogram(initial_data) == expected_result
