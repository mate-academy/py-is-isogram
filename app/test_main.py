import pytest

from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word, expected_result",
        [
            pytest.param("", True, id="the empty string"),
            pytest.param("playgrounds", True, id="has no repeating letters"),
            pytest.param("look", False, id="has repeating lower letters"),
            pytest.param("Adam", False, id="should be case-insensitive"),
        ]
    )
    def test_should_check_is_isogram(self, word, expected_result):
        assert is_isogram(word) == expected_result
