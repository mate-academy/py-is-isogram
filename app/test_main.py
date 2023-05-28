import pytest


from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word,expected_result",
        [
            pytest.param(
                "", True, id="Empty string should return True"
            ),
            pytest.param(
                "gEometry", False, id="Should be case-insensitive"
            ),
            pytest.param(
                "playgrounds", True, id="Should return correct result"
            ),
            pytest.param(
                "zoom", False, id="Consecutive letters should be count as non-isogram"
            )
        ]
    )
    def test_should_return_correct_result(self, word, expected_result):
        assert is_isogram(word) == expected_result
