import pytest
from app.main import is_isogram

class TestIsIsogram:
    @pytest.mark.parametrize(
        "word,expected_result",
        [
            pytest.param(
                "", True,
                id="should return True when empty string"
            ),
            pytest.param(
                "playgrounds", True,
                id="should return True when the word is isogram"
            ),
            pytest.param(
                "look", False,
                id="should return False when the word isn't isogram"
            ),
            pytest.param(
                "Adam", False,
                id="should be case insensitive"
            )
        ]
    )
    def test_should_return_right_result(
            self,
            word: str,
            expected_result: bool
    ) -> None:
        assert is_isogram(word) == expected_result
