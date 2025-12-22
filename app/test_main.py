import pytest

from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word,expected_result", [
            pytest.param(
                "playgrounds",
                True,
                id="Should return True"
            ),
            pytest.param(
                "look",
                False,
                id="Should return False"
            ),
            pytest.param(
                "Adam",
                False,
                id="Should return False"
            ),
            pytest.param(
                "",
                True,
                id="Should return True when word is empty"
            )
        ]
    )
    def test_is_isogram(self, word, expected_result):
        assert is_isogram(word) == expected_result
