import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, boolean_value",
    [
        pytest.param('pythonist', False, id="Not an isogram"),
        pytest.param('must', True, id="True isogram"),
        pytest.param('be', True, id="True isogram"),
        pytest.param('lazy', True, id="True isogram"),
        pytest.param('alwAys', False, id="Not an isogram with different registers"),
        pytest.param('anD', True, id="True isogram with different registers"),
        pytest.param('EvERywhEre', False, id="Not an isogram with different registers"),
    ],
)
def test_word_variations_is_isogram(word, boolean_value):
    assert is_isogram(word) == boolean_value


def test_if_string_is_empty():
    assert is_isogram('') is True
