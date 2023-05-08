import pytest
from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "accept_str, result",
        [
            pytest.param(
                "playgrounds",
                True,
                id="check if exist repeated words"
            ),
            pytest.param(
                "look",
                False,
                id="check if exist repeated words"
            ),
            pytest.param(
                "Adam",
                False,
                id="check if exist repeated words"
            ),
            pytest.param(
                "",
                True,
                id="Empty str is isogram"
            )
        ]

    )
    def test_str_is_isogram(
            self,
            accept_str: str,
            result: bool
    ) -> None:
        assert is_isogram(accept_str) == result

    @pytest.mark.parametrize(
        "value, expected_error",
        [
            pytest.param(
                123445,
                AttributeError,
                id="value should be str not int"
            )
        ]
    )
    def test_is_value_str(
            self,
            value: str, expected_error: AttributeError
    ) -> None:
        with pytest.raises(expected_error):
            is_isogram(value)
