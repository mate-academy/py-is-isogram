from app.main import is_isogram
import pytest


@pytest.mark.parametrize('test_input, expected',
                         [
                             ('playgrounds', True),
                             ('look', False),
                             ('Adam', False),
                             (' ', True),
                         ]
                         )
def test_is_isogram(test_input, expected):
    assert is_isogram(test_input) == expected
