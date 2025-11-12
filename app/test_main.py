from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word, bools",
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
def test_is_isogram(word: str, bools: bool) -> None:
    assert is_isogram(word) == bools
