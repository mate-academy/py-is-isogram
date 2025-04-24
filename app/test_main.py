import pytest
from app.main import is_isogram


@pytest.mark.parametrize("word, expected", [
    ('playgrounds', True),
    ('look', False),
    ('Adam', False),
    ('', True),
    ('abcdefg', True),
    ('A', True),
    ('Aa', False),
    ('unique', False),
    ('repeated', False),
    ('Noon', False),
    ('Python', True),
    ('PythoN', True),
])
def test_is_isogram(word, expected):
    assert is_isogram(word) == expected
