import pytest
from app.main import is_isogram


class TestIsIsogram:

    @pytest.mark.parametrize(
        "word,expected",
        [
            pytest.param(
                "playgrounds",
                True,
                id="all letters different"
            ),
            pytest.param(
                "look",
                False,
                id="repeated letters"
            ),
            pytest.param(
                "Adam",
                False,
                id="case insensitive"
            ),
            pytest.param(
                "",
                True,
                id="empty string case"
            ),
            pytest.param(
                "ab",
                True,
                id="two difference letters"
            ),
            pytest.param(
                "aa",
                False,
                id="two same letters"
            ),
            pytest.param(
                "a",
                True,
                id="one letter case"
            )
        ]
    )
    def test_is_isogram_detection(
            self,
            word: str,
            expected: bool
    ) -> None:

        assert is_isogram(word) == expected
