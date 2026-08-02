import pytest
from app.main import is_isogram


class TestStringIsogram:
    @pytest.mark.parametrize(
        "entered_string,expected_result",
        [
            pytest.param(
                "",
                True,
                id="empty string"
            ),
            pytest.param(
                "MoM",
                False,
                id="check for uppercase letters"
            ),
            pytest.param(
                "playgrounds",
                True,
                id="check with large number of characters"
            ),
            pytest.param(
                "gEneral",
                False,
                id="string with different cases of the "
                "same letter is not an isogram"
            )
        ]
    )
    def test_general_function(
        self,
        entered_string: str,
        expected_result: bool
    ) -> None:
        result = is_isogram(entered_string)
        assert result == expected_result
