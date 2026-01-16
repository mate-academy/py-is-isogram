from app.main import is_isogram
import pytest


class TestIsIsogram:
    @pytest.mark.parametrize(
        "inputt, expected_result",
        [
            pytest.param(
                "sSS",
                False,
                id="lower + upper case"
            ),
            pytest.param(
                "gggggg",
                False,
                id="many equal letters"
            ),
            pytest.param(
                "ee",
                False,
                id="typical require"
            ),
            pytest.param(
                "Ee",
                False,
                id="one lower and one upper"
            ),
            pytest.param(
                "lower",
                True,
                id="lower word"
            ),
            pytest.param(
                "UPPER",
                False,
                id="upper word"
            ),
            pytest.param(
                "t34tferrR",
                False,
                id="string with numbers"
            ),
            pytest.param(
                "58gu_(&^50gv*",
                False,
                id="some signs"
            ),
            pytest.param(
                "!@#$%&*(",
                True,
                id="no letters"
            ),
            pytest.param(
                "111",
                False,
                id="only numbers"
            ),
            pytest.param(
                "",
                True,
                id="empty line"
            )
        ]
    )
    def test_is_isogram_correct_output(
            self,
            inputt: str,
            expected_result: bool
    ) -> None:
        assert is_isogram(inputt) == expected_result

    @pytest.mark.parametrize(
        "inputt, expected_error",
        [
            pytest.param(
                1,
                AttributeError,
                id="integer"

            ),
            pytest.param(
                2.9,
                AttributeError,
                id="float"
            ),
            pytest.param(
                ["ss"],
                AttributeError,
                id="list"
            ),
            pytest.param(
                None,
                AttributeError,
                id="none"
            )
        ]
    )
    def test_raising_errors_correctly(
            self,
            inputt: str,
            expected_error: Exception
    ) -> None:
        with pytest.raises(expected_error):
            is_isogram(inputt)
