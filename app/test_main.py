from app.main import is_isogram
import pytest


@pytest.mark.parametrize("word, result", [
    ("loop", False),
    ("Ave", True),
    ("Adam", False),
    ("Dance", True),
    ("", True),
])
def test_result(word: str, result: bool) -> None:
    assert is_isogram(word) == result
