import pytest
from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word,expected",
        [
            pytest.param(
                "", True,
                id="empty string is an isogram"
            ),
            pytest.param(
                "look", False,
                id="letters cannot repeat"
            ),
            pytest.param(
                "Adam", False,
                id="Different cases letters cannot repeat"
            ),
            pytest.param(
                "playgrounds", True,
                id="lower cased letters"
            ),
            pytest.param(
                "ToXiC", True,
                id="lower and upper cased letters"
            ),

        ]
    )
    def test_is_isogram(
            self,
            word: str,
            expected: bool
    ) -> None:
        assert is_isogram(word) == expected
