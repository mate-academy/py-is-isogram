import pytest

from app.main import is_isogram


class TestIsIsogram:

    @pytest.mark.parametrize(
        "word, answer",
        [
            pytest.param(
                "playgrounds",
                True,
                id="should return 'True'"
            ),
            pytest.param(
                "",
                True,
                id="should return 'True'"
            ),
            pytest.param(
                "look",
                False,
                id="should return 'False'"
            ),
            pytest.param(
                "Adam",
                False,
                id="should return 'False'"
            ),
            pytest.param(
                "AAA",
                False,
                id="should return 'False'"
            ),
        ]
    )
    def test_is_isogram(
            self,
            word: str,
            answer: bool
    ) -> None:
        assert is_isogram(word) == answer
