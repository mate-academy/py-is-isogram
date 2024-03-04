from app.main import is_isogram
import pytest


class TestIsIsogram:
    @pytest.mark.parametrize(
        "string, expected_result",
        [
            pytest.param(
                "playgrounds",
                True
            ),
            pytest.param(
                "look",
                False
            ),
            pytest.param(
                "Adam",
                False
            ),
            pytest.param(
                "",
                True
            )
        ]
    )
    def test_is_isogram(
            self,
            string: str,
            expected_result: bool
    ) -> None:
        assert is_isogram(string) == expected_result
