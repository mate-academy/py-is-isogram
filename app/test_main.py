import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [("playgrounds", True),
     ("look", False),
     ("Adam", False),
     ("", True),
     ("123", True),
     ("112", False),
     ("%^&*", True)
     ]
)
def test_is_isogram(word, expected):
    assert is_isogram(word) is expected
