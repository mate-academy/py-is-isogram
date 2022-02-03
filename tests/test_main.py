import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, boolean_value",
    [
        ('pythonist', False),
        ('must', True),
        ('be', True),
        ('lazy', True),
        ('alwAys', False),
        ('anD', True),
        ('EvERywhEre', False),
    ],
)
def test_word_variations_is_isogram(word, boolean_value):
    assert is_isogram(word) == boolean_value


def test_if_string_is_empty():
    assert is_isogram('') is True