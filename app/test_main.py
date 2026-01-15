from app.main import is_isogram
import pytest


class TestPositiveValues:
    @pytest.mark.parametrize(
        "input_word, result",
        [
            pytest.param(
                "playgrounds",
                True,
                id="Test when word is iso-gram"),
            pytest.param(
                "",
                True,
                id="Test when input word is empty ")
        ]
    )
    def test_is_iso_gram_for_positive_value(
            self,
            input_word: str,
            result: bool) -> None:
        assert (is_isogram(input_word) == result), \
            (f"Output value {is_isogram(input_word)} "
             f"should be equal to {result}")


class TestNegativeValues:
    @pytest.mark.parametrize(
        "input_word, result",
        [
            pytest.param(
                "look",
                False,
                id="Test when input word is not iso-gram"),
            pytest.param(
                "Adam",
                False,
                id="Test when input word has upper case")
        ]
    )
    def test_is_iso_gram_for_negative_value(
            self,
            input_word: str,
            result: bool) -> None:
        assert (is_isogram(input_word) == result), \
            (f"Output value {is_isogram(input_word)} "
             f"should be equal to {result}")
