import pytest
from app.main import is_isogram
from typing import Any


class TestIsIsogram:

    @pytest.mark.parametrize(
        "word,expected_result",
        [
            pytest.param(
                "playgrounds",
                True,
                id="should return True when no repeating letters"
            ),
            pytest.param(
                "look",
                False,
                id="should return False for repeating letters "
            ),
            pytest.param(
                "Adam",
                False,
                id="should count both uppercase and lowercase letters"
            ),
            pytest.param(
                "",
                True,
                id="should return True for an empty string"
            )
        ]
    )
    def test_define_isogram_correctly(
            self,
            word: str,
            expected_result: bool
    ) -> None:
        assert is_isogram(word) == expected_result


