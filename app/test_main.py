import pytest

from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word, expected_result",
        [
            pytest.param("playgrounds", True),
            pytest.param("look", False),
            pytest.param("Adam", False),
            pytest.param("", True),
            pytest.param(" ", True),
            pytest.param("  ", False),
        ]
    )
    def test_is_isogrsm(self, word: str, expected_result: bool) -> None:
        assert is_isogram(word) == expected_result
