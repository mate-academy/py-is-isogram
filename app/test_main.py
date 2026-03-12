import pytest
from app.main import is_isogram


class TestIsIsogram:

    @pytest.mark.parametrize(
        "input_value,needed_value",
        [
            pytest.param(
                "playgrounds",
                True,
                id="should return T for isogram word"
            ),
            pytest.param(
                "look",
                False,
                id="should return F for isogram word"
            ),
            pytest.param(
                "Adam",
                False,
                id="should return F for non-isogram with different cases"
            ),
            pytest.param(
                "",
                True,
                id="should return T for empty input"
            ),
        ]
    )
    def test_should_return_propper_output(
            self,
            input_value: str,
            needed_value: bool
    ) -> None:
        assert is_isogram(input_value) is needed_value
