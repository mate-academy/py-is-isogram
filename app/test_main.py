import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("ISOGRAM", True),
    ],
    ids=["Isogram word",
         "Not isogram word",
         "First letter is upper in not isogram word",
         "Empty string is isogram",
         "All letters are upper in isogram word"]
)
def test_get_coin_combination(word: str, expected: bool) -> None:
    assert is_isogram(word) is expected
