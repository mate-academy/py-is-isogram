import pytest

from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word, expected_result",
        [
            pytest.param(
                "playground", True,
                id="Should return True"
            ),
            pytest.param(
                "look", False,
                id="Should return False"
            ),
            pytest.param(
                "Adam", False,
                id="Should return False"
            ),
            pytest.param(
                "", True,
                id="Should return True"
            )
        ]
    )
    def test_if_is_isogram_works_correctly(
        self,
        word,
        expected_result
    ):
        assert is_isogram(word) == expected_result
