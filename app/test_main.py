from app.main import is_isogram
import pytest


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word,bool_res",
        [
            pytest.param(
                "", True, id="return true if empty string"
            ),
            pytest.param(
                "Adam", False, id="return false if case-insensitive"
            ),
            pytest.param(
                "playgrounds", True, id="check for 'True'"
            ),
            pytest.param(
                "look", False, id="check for 'False'"
            )
        ]
    )
    def test_implementation_function(
            self,
            word: str,
            bool_res: bool
    ) -> None:
        assert is_isogram(word) == bool_res
