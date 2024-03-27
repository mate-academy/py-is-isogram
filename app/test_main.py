import pytest
from app.main import is_isogram


class TestIsIsogram:

    @pytest.mark.parametrize(
        "word, result",
        [
            pytest.param(
                "", True
            ),
            pytest.param(
                "playgrounds", True
            ),
            pytest.param(
                "look", False
            ),
            pytest.param(
                "Adam", False
            )
        ]
    )
    def test_check_correct_output(
        self,
        word: str,
        result: bool
    ) -> None:
        assert is_isogram(word) == result
