import pytest

from app.main import is_isogram


@pytest.mark.parametrize('test_input,expected', [
    "playgrounds", True,
    "look", True,
    "Adam", True,
    "",
])

def test_is_isogram(test_input, expected):
    assert is_isogram(test_input) == expected
