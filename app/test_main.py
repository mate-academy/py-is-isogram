import pytest

from app.main import is_isogram


class TestIsIsogram:
    @pytest.mark.parametrize(
        "word,output",
        [
            ('', True),
            ('Adam', False),
            ('look', False),
            ('playgrounds', True),
            ('abracadabra', False),
            ('After', True)
        ]
    )
    def test_correct_output(
            self,
            word,
            output
    ):
        assert is_isogram(word) == output
