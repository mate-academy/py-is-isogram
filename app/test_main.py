from app.main import is_isogram
import pytest


@pytest.mark.parametrize("word,result",
                         [
                             ("", True),
                             ("ROLF", True),
                             ("Adam", False),
                             ("apple", False)
                         ])
def test_check_empty_string(word: str,
                            result: bool) -> None:
    assert is_isogram(word) == result
