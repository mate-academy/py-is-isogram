import pytest
from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "arg_string,result",
        [

            pytest.param(
                "playgrounds",
                True,
                id="test_non_consecutive_letters_are_not_isogram"
            ),
            pytest.param(
                "look",
                False,
                id="test_consecutive_letters_are_not_isogram"
            ),
            pytest.param(
                "",
                True,
                id="test_empty_string_is_isogram"
            ),
            pytest.param(
                "Adam",
                False,
                id="test_isogram_is_case_insensitive"
            )
        ]

    )
    def test_modify_classes_correctly(
            self,
            arg_string: str,
            result: bool
    ) -> None:
        assert is_isogram(arg_string) == result
