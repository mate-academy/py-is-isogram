from typing import Any
import pytest

from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word, is_word_isogram",
        [
            pytest.param(
                "playgrounds",
                True,
                id="if word is isogram"
            ),
            pytest.param(
                "CrIngE",
                True,
                id="word is isogram case-insensitive"
            ),
            pytest.param(
                "brothers",
                False,
                id="if word is not isogram"
            ),
            pytest.param(
                "Calc",
                False,
                id="with upper and lower letters"
            ),
            pytest.param(
                "JONNY",
                False,
                id="just upper letters"
            ),
            pytest.param(
                "",
                True,
                id="if word is empty"
            )
        ]
    )
    def test_different_word_input(
            self,
            word: str,
            is_word_isogram: bool
    ) -> None:
        assert is_isogram(word) == is_word_isogram

    @pytest.mark.parametrize(
        "incorrect_word, expected_error",
        [
            pytest.param(
                (232, {}, [], ()),
                AttributeError,
                id="incorrect argument 'word'"
            )
        ]
    )
    def test_for_incorrect_argument(
            self,
            incorrect_word: Any,
            expected_error: AttributeError
    ) -> None:
        for cents in incorrect_word:
            with pytest.raises(expected_error):
                is_isogram(incorrect_word)
