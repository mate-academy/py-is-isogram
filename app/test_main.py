import pytest
from app.main import is_isogram


class TestIsIsogram:

    @pytest.mark.parametrize(
        "word,expected_result",
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
                "a",
                True,
                id="one letter case"
            ),
            pytest.param(
                "ab",
                True,
                id="two difference letters"
            ),
            pytest.param(
                "aa",
                False,
                id="two similar letters"
            )
        ]
    )
    def test_is_isogram_detection(
            self,
            word: str,
            expected_result: bool
    ) -> None:
        result = is_isogram(word)

        assert result == expected_result
