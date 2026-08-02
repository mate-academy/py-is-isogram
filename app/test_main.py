import pytest

from app.main import is_isogram


class TestCorrectResults:

    @pytest.mark.parametrize(
        "expected_string,expected_output",
        [
            pytest.param(
                "playgrounds",
                True,
                id="must not be repeating letters"
            ),
            pytest.param(
                "look",
                False,
                id="must be repeating letters"
            ),
            pytest.param(
                "Adam",
                False,
                id="must be repeating letters in different case latter"
            ),
            pytest.param(
                "",
                True,
                id="return True if get an empty string"
            ),
        ]
    )
    def test_isogram_is_correctly(
            self,
            expected_string: str,
            expected_output: bool
    ) -> None:
        assert is_isogram(expected_string) == expected_output

    @pytest.mark.parametrize(
        "expected_string_with_number,excepted_error",
        [
            pytest.param(
                "playground1",
                ValueError,
                id="should be only letters"
            ),
        ]
    )
    def test_raised_correctly_error(
            self,
            expected_string_with_number: str,
            excepted_error: Exception
    ) -> None:
        with pytest.raises(excepted_error):
            is_isogram(expected_string_with_number)
