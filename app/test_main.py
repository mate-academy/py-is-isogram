from app.main import is_isogram
import pytest
from typing import List


# Тест чи слова є isogram
@pytest.mark.parametrize(
    "word, excepted",
    [
        ("playgrounds", True),
        ("", True),
        ("look", False),
        ("Adam", False),
        ("Dermatoglyphics", True),
    ],
)
def test_is_isogram(
        word: str,
        excepted: List[list]
) -> None:
    assert is_isogram(word) is excepted
