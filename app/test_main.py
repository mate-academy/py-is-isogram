from app.main import is_isogram

import pytest

class TestIsIsogram:
    @pytest.mark.parametrize(
        "input_value, expected",
        [
            ('playgrounds', True),
            ('look', False),
            ('', True),
            ('Adam', False),
            ('A', True)

        ]
    )
    def test_is_isogram(self, input_value: str, expected: bool):
        assert (is_isogram(input_value) == expected)
