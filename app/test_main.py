from app.main import is_isogram
from pytest import mark, param


class TestIsIsogram:
    @mark.parametrize(
        "input_string, expected_result",
        [
            param(
                "",
                True,
                id="Empty string should be an isogram",
            ),

            param(
                "playgrounds",
                True,
                id="Word with no repeating letters should be an isogram",
            ),

            param(
                "Adam",
                False,
                id="Should be case insensitive",
            ),

            param(
                "look",
                False,
                id="Letters must not be repeated",
            )
        ]
    )
    def test_should_return_correct_boolean_value(
            self,
            input_string: str,
            expected_result: bool
    ) -> None:
        assert is_isogram(input_string) is expected_result
