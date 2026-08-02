import pytest

from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word, expected",
        [
            pytest.param(
                "playgrounds", True,
                id="playgrounds is an isogram"
            ),
            pytest.param(
                "look", False,
                id="look is not an isogram"
            ),
            pytest.param(
                "Adam", False,
                id="Adam is not an isogram, two 'a' in this word"
            ),
            pytest.param(
                "", True,
                id="Empty string is an isogram"
            )
        ]
    )
    def test_is_isogram(self, word: str, expected: bool) -> None:
        assert is_isogram(word) == expected
