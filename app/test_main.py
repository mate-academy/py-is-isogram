import pytest

from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word,result",
        [
            pytest.param("playgrounds", True, id="Result True"),
            pytest.param("look", False, id="Result False"),
            pytest.param("Adam", False, id="Result False"),
            pytest.param("", True, id="Result True")
        ]
    )
    def test_different_parameters(
            self,
            word: str,
            result: bool
    ) -> None:
        assert is_isogram(word) == result
