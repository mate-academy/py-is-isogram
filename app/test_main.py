import pytest

from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "input_string,expected_value",
        [
            pytest.param(
                "playgrounds",
                True,
                id="Must be 'True' for normal value"
            ),
            pytest.param(
                "look",
                False,
                id="Must be 'False' for double letter 'o'"
            ),
            pytest.param(
                "Adam",
                False,
                id="upper and lower letter is the same letter"
            ),
            pytest.param(
                "",
                True,
                id="empty string must be 'isogram'"
            ),
        ]
    )
    def test_is_isogram(self, input_string: str, expected_value: bool) -> None:
        assert is_isogram(input_string) == expected_value
