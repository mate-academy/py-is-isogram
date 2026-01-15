from app.main import is_isogram
import pytest


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word, expected_res", [
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
    def test_is_isogram(self, word: str, expected_res: bool) -> None:
        assert is_isogram(word) == expected_res
