import pytest

from app.main import is_isogram


class TestIsIsogram:

    @pytest.mark.parametrize(
        "word,expected_result",
        [
            pytest.param(
                "",
                True,
                id="should check empty string is True"
            ),

            pytest.param(
                "Jake",
                True,
                id="should function work"
            ),

            pytest.param(
                "playground",
                True,
                id="should check long word"
            ),

            pytest.param(
                "look",
                False,
                id="should check word isn't isogram"
            ),

            pytest.param(
                "Adam",
                False,
                id="should check letters repeating after another one"
            )
        ]
    )
    def test_is_word_an_isogram(
            self,
            word: str,
            expected_result: bool
    ) -> None:
        assert is_isogram(word) == expected_result
