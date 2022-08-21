import pytest

from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "given_word, expected_word",
        [
            ("playgrounds", True),
            ("look", False),
            ("Adam", False),
            ("", True)
        ]
    )
    def test_is_isogram(self, given_word, expected_word):
        assert is_isogram(given_word) == expected_word
