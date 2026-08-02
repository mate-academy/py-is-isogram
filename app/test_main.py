import pytest
from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word",
        [
            pytest.param(
                "sometext"
            )
        ]
    )
    def test_should_return_bool(self, word: str) -> None:
        assert isinstance(is_isogram(word), bool)

    @pytest.mark.parametrize(
        "word,expected_output",
        [
            pytest.param(
                "Adam", False,
                id="function should be case-insensitive"
            ),
            pytest.param(
                "", True,
                id="empty string should return True"
            ),
            pytest.param(
                "look", False,
                id="consecutive letters should return False"
            ),
        ]
    )
    def test_should_return_correct_value(
            self,
            word: str,
            expected_output: bool
    ) -> None:
        assert is_isogram(word) == expected_output

    @pytest.mark.parametrize(
        "word,expected_error",
        [
            pytest.param(
                99,
                AttributeError
            )
        ]
    )
    def test_should_raising_errors_correctly(
            self,
            word: any,
            expected_error: TypeError
    ) -> None:
        with pytest.raises(expected_error):
            is_isogram(word)
