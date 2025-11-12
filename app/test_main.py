from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word, bool",
    [
        ("playgrounds", True),
        ("Adam", False),
        ("look", False),
        ("ABOMUS", True),
        ("dermatoglyphics!!", False),
        ("", True)
    ],
    ids=[
        "correct word playgrounds",
        "wrong word Adam",
        "wrong word look",
        "word out of capitals",
        "word with symbol !",
        "empty string"
    ]
)
def test_is_isogram(word, bool):
    assert is_isogram(word) == bool
