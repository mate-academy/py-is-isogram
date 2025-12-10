import pytest
from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word,expected",
        [
            pytest.param(
                "playgrounds",
                True,
                id="isogram must return True"
            ),
            pytest.param(
                "look",
                False,
                id="not isogram must return False"
            ),
            pytest.param(
                "Adam",
                False,
                id="func must be case insensitive"
            ),
            pytest.param(
                "",
                True,
                id="'' is isogram"
            )
        ]
    )
    def test_is_isogram(
            self,
            word: str,
            expected: bool
    ) -> None:
        assert is_isogram(word) == expected
