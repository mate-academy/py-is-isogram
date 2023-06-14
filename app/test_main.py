import pytest

from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word, expected_result",
        [
            pytest.param("", True, id="return True for empty string"),
            pytest.param("a", True, id="return True for one letter"),
            pytest.param(
                "playgrounds", True, id="return True for long word"
            ),
            pytest.param(
                "look", False, id="return False if letters duplicated"
            ),
            pytest.param(
                "Adam",
                False,
                id="return False if letters duplicated and different cases",
            ),
        ],
    )
    def test_check_word_correctly(
        self, word: str, expected_result: bool
    ) -> None:
        assert is_isogram(word) == expected_result
