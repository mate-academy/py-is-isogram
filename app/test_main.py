import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected",
    [("look", False),
     ("", True),
     ("Playground", True),
     ("Adam", False),
     ("abc1", False),
     ("abc-", False),


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
                             {"word": 10}
                         ]
                         )
def test_is_isogram_non_string_raises(bad_input: object):
    with pytest.raises(AttributeError):
        is_isogram(bad_input)
