from app.main import is_isogram

import pytest


@pytest.mark.parametrize(
    "word, expected",
    [
        pytest.param('', True,
                     id="empty_string"),
        pytest.param('a', True,
                     id="single_letter"),
        pytest.param('playgrounds', True
            , id="no_repeating_letters"),
        pytest.param('subdermatoglyphic', True,
                     id="long_isogram"),
        pytest.param('ab', True,
                     id="two_different_letters"),
        pytest.param('look', False,
                     id="repeating_letters"),
        pytest.param('Adam', False,
                     id="case_insensitive_A_a"),
        pytest.param('MoOse', False,
                     id="case_insensitive_O_o"),
        pytest.param('aaaa', False,
                     id="all_same_letters"),
        pytest.param('aa', False,
                     id="two_same_letters"),
        pytest.param('Dermatoglyphics', True,
                     id="mixed_case_isogram"),
        pytest.param('aba', False,
                     id="non_consecutive_repeat"),
        pytest.param('z', True,
                     id="single_uppercase_Z"),
        pytest.param('Zz', False,
                     id="same_letter_different_case"),
    ],
)
def test_is_isogram(word, expected):
    assert is_isogram(word) is expected
