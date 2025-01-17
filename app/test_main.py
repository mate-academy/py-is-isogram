import pytest
from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word, result",
        [
            pytest.param(
                "",
                True,
                id="empty string case"
            ),
            pytest.param(
                "Adam",
                False,
                id="case insensitivity"
            ),
            pytest.param(
                "subdermatoglyphic",
                True,
                id="should return True if the word is isogram"
            ),
            pytest.param(
                "look",
                False,
                id="should return False if the word isn't isogram"
            )
        ]
    )
    def test_is_isogram(
            self,
            word: str,
            result: bool
    ) -> None:
        assert is_isogram(word) == result
