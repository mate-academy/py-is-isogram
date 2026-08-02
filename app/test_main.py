import pytest

from app.main import is_isogram


class TestIsIsogram:

    @pytest.mark.parametrize(
        "initial_str, expected_result",
        [
            pytest.param(
                "look",
                False,
                id="should return false repeating letters (consecutive)"
            ),
            pytest.param(
                "paradise",
                False,
                id="should return false repeating letters (non-consecutive)"
            ),
            pytest.param(
                "",
                True,
                id="should return true when input is empty str"
            ),
            pytest.param(
                "ADad",
                False,
                id="should return false while same letter different registers"
            ),
            pytest.param(
                "Hello, beautiful,",
                False,
                id="should return false while repeating punctual marks"
            ),
            pytest.param(
                "Hey,   Mark",
                False,
                id="should return false while repeating white spaces"
            )
        ]
    )
    def test_returns_correct_answer(self, initial_str, expected_result):
        result = is_isogram(initial_str)
        assert result is expected_result
