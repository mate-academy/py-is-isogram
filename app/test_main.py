import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,isogram",
    [
        ("", True),
        ("playgrounds", True),
        ("look", False),
        ("DIanA", False),
        ("PYthON", True),
        (" ", True),
        ("  ", False),
    ],
    ids=[
        "Empty string should return True",
        "`playgrounds` should return True",
        "`look` should return False",
        "`DIanA` should return False",
        "`PYthON` should return True",
        "White space should return True",
        "2 white spaces should return False",
    ]
)
def test_checking_correctly(
        word: str,
        isogram: bool
) -> None:
    assert is_isogram(word) == isogram
