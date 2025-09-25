import pytest
from app.main import is_isogram
from typing import Union


@pytest.mark.parametrize(
    "word,expected",
    [("look", False),
     ("", True),
     ("Playground", True),
     ("Adam", False),


     ]
)
def test_is_isogram_(word, expected) -> None:
    assert is_isogram(word) is expected
    assert isinstance(is_isogram(word), bool)


@pytest.mark.parametrize("bad_input",
                         [
                             3.5,
                             10,
                             None,
                             [1],
                             {"word": 10},
                             "abc1"
                         ]
                         )
def test_is_isogram_non_string_raises(bad_input: object):
    with pytest.raises(TypeError):
        is_isogram(bad_input)
