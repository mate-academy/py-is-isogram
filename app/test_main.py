import pytest

from app.main import is_isogram


class TestMain:
    @pytest.mark.parametrize(
        "word,result",
        [
            pytest.param(
                "", True,
                id="should return 'True' when word is empty string"
            ),
            pytest.param(
                "playgrounds", True,
                id="should return 'True' when word is isogram"
            ),
            pytest.param(
                "look", False,
                id="should return 'False' when word has repeating letters"
            ),
            pytest.param(
                "Adam", False,
                id="function should be case-insensitive"
            ),

        ]
    )
    def test_is_isogram(self, word: str, result: bool) -> None:
        assert is_isogram(word) == result
