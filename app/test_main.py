import pytest

from app.main import is_isogram


class TestIsogram:
    @pytest.mark.parametrize(
        "word_to_check, result",
        [
            pytest.param(
                "playgrounds",
                True
            ),
            pytest.param(
                "look",
                False
            ),
            pytest.param(
                "Adam",
                False
            ),
            pytest.param(
                "",
                True
            )
        ]
    )
    def test_should_check_the_word(
            self,
            word_to_check: str,
            result: bool
    ) -> None:
        assert is_isogram(word_to_check) == result
