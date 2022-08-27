import pytest
from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word, expected_result",
        [
            pytest.param("playgrounds", True, id="Checking long word"),
            pytest.param("look", False, id="checking double 'o'"),
            pytest.param("Adam", False, id="checking title word"),
            pytest.param("", True, id="empty str")
        ]
    )
    def test_is_isogram(
            self, word, expected_result):
        assert is_isogram(word) == expected_result
