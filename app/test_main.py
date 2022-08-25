import pytest
from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "initial_word, expected_word",
        [
            ('playgrounds', True),
            ('PLAYgrounds', True),
            ('look', False),
            ('Adam', False),
            ('', True),
        ]
    )
    def test_is_isogram_validation(self, initial_word, expected_word):
        assert is_isogram(initial_word) == expected_word
