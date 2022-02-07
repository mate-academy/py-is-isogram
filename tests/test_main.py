import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    'word, result',
    [
        ['', True],
        ['nazr', True],
        ['mdM', False]
    ]
)
def test_is_isogram(word, result):
    assert is_isogram(word) == result
