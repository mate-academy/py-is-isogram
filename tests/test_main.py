from string import ascii_lowercase
from random import randint, sample

from app.main import is_isogram


def test_empty_string():
    assert is_isogram('')


def test_isogram_string():
    tested_string_list = sample(
        ascii_lowercase,
        randint(1, len(ascii_lowercase))
    )
    tmp = ''
    for letter in tested_string_list:
        if randint(0, 1):
            tmp += letter.upper()
        else:
            tmp += letter.lower()
    tested_string = tmp
    assert is_isogram(tested_string)


def test_non_isogram_string():
    tested_string = ''.join(sample(
        ascii_lowercase,
        randint(2, len(ascii_lowercase))
    ))

    tested_string += ''.join(sample(tested_string, 2))

    assert not is_isogram(tested_string)
