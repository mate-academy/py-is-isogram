from app.main import is_isogram
import pytest

class TestIsogram:

    @pytest.mark.parametrize(
        "testing_string, expected_result",
        (
            ("playgrounds", True),
            ("look", False),
            ("Adam", False),
            ("", True)
        )
    )
    def test_is_isogram_should_return_correct_values(
        self,
        testing_string: str,
        expected_result: bool
    ) -> None:
        assert is_isogram(testing_string) == expected_result

    @pytest.mark.parametrize(
        "testing_value, expected_error",
        (
            (1, AttributeError),
        )
    )
    def test_is_isogram_rise_correct_errors(
        self,
        testing_value: int,
        expected_error: type
    ) -> None:
        with pytest.raises(expected_error):
            is_isogram(testing_value)