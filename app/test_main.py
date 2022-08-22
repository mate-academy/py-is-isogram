from app.main import is_isogram
import pytest


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word,expected_value",
        [
            ('playgrounds', True),
            ('look', False),
            ('Adam', False),
            ('', True)
        ]
    )
    def test_should_return_valid_value(self, word, expected_value):
        result = is_isogram(word)
        assert result == expected_value
