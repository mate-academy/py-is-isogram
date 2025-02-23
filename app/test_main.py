import pytest
from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "string, expected_result",
        [
            pytest.param(
                "playgrounds",
                True,
                id="'playgrouns' is an isogram."
            ),
            pytest.param(
                "look",
                False,
                id="'look' is not an isogram."
            ),
            pytest.param(
                "Adam",
                False,
                id="'Adam' is not an isogram."
            ),
            pytest.param(
                "",
                True,
                id="An empty string should be an isogram."
            )
        ]
    )
    def test_is_isogram(
                        self,
                        string: str,
                        expected_result: bool
    ) -> None:
        assert is_isogram(string) == expected_result
