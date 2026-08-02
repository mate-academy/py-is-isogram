from app.main import is_isogram

import pytest


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word,expected_result",
        [
            pytest.param("", True, id="should return True for empty string"),
            pytest.param("Adam", False, id="should return True for 'Adam'"),
            pytest.param("look", False, id="should return True for 'look'"),
            pytest.param(
                "playgrounds",
                True,
                id="should return True for 'playgrounds'"
            ),
        ],
    )
    def test_is_isogram(self, word: str, expected_result: bool) -> None:
        assert is_isogram(word) == expected_result
