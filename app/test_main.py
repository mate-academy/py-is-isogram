from app.main import is_isogram
import pytest


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word, expected_result",
        [
            pytest.param(
                "playgrounds", True, id="all_small_different_letters"
            ),
            pytest.param(
                "Kok", False, id="all_different_with_one_big_is_same"
            ),
            pytest.param("", True, id="empty_line_is_good"),
            pytest.param("look", False, id="two same consecutive"),
        ],
    )
    def test_only_letters_in_word(
        self, word: str, expected_result: bool
    ) -> bool:
        result = is_isogram(word)
        assert result == expected_result
