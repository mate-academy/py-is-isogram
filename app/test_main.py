import pytest

from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "initial_word, expected_result",
        [
            pytest.param(
                "PLAYgrounds",
                True,
                id="all chars are different"
            ),
            pytest.param(
                "",
                True,
                id="empty line is Isogram"
            ),
            pytest.param(
                "Adam",
                False,
                id="can`t repeat chars in Isogram"
            ),
            pytest.param(
                "look",
                False,
                id="consecutive letters are not an Isogram"
            )
        ]
    )
    def test_check_is_isogram_correctly(
            self,
            initial_word,
            expected_result
    ):
        assert is_isogram(initial_word) == expected_result
