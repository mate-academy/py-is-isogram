import pytest

from app.main import is_isogram


class TestIsogram:
    @pytest.mark.parametrize(
        "word,expected",
        [
            pytest.param(
                "playgrounds",
                True,
                id="'playgrounds' is True"
            ),
            pytest.param(
                "look",
                False,
                id="'look' is False"
            ),
            pytest.param(
                "Adam",
                False,
                id="'Adam' is False"
            ),
            pytest.param(
                "",
                True,
                id="'' is True"
            ),
            pytest.param(
                "Playgrounds",
                True,
                id="'Playgrounds' is True"
            )
        ]
    )
    def test_check_word(self, word: str, expected: bool) -> None:
        assert is_isogram(word) == expected
