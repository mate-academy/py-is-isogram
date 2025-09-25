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
def test_is_isogram_non_string_raise(
        bad_input: Union[
            float,
            int,
            list,
            dict,
            str,
            None
        ]) -> None:
    with pytest.raises(TypeError):
        is_isogram(word=bad_input)
