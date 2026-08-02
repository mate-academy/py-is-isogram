from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word,expected_error",
    [
        pytest.param(
            "", True,
            id="should be error if empty line is Flase",
        ),
        pytest.param(
            'Adam', False,
            id="should be error if adam is True",
        ),
        pytest.param(
            'look', False,
            id="should be error if look is True"
        ),
        pytest.param(
            'playgrounds', True,
            id="should be error if word is False"
        ),
    ]
)
def test_for_no_double_literal(word, expected_error):
    assert is_isogram(word) == expected_error
