import pytest
from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word, expected",
        [
            pytest.param(
                "playgrounds",
                True,
                id="is_isogram str",
            ),
            pytest.param(
                "look",
                False,
                id="is not isogram 2 'o'",
            ),
            pytest.param(
                "Adam",
                False,
                id="is not isogram 2 'a'",
            ),
            pytest.param(
                "",
                True,
                id="is isogram 0 letters",
            )
        ]
    )
    def test_is_isogram(self, word: str, expected: bool) -> None:
        assert is_isogram(word) == expected
