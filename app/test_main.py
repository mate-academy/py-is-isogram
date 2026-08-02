import pytest

from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word, expected_result",
        [
            pytest.param(
                "playgrounds",
                True,
                id="Should return True if the word is an isogram."
            ),
            pytest.param(
                "",
                True,
                id="Should return True if the word is an empty string."
            ),
            pytest.param(
                "look",
                False,
                id="Should return False if the word has repeating letters."
            ),
            pytest.param(
                "Adam",
                False,
                id="The function should be case-insensitive."
            )
        ]
    )
    def test_is_isogram(
            self,
            word: str,
            expected_result: bool
    ) -> None:
        assert is_isogram(word) == expected_result
