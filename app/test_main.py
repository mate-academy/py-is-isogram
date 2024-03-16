import pytest
from app.main import is_isogram


@pytest.mark.parametrize("word, expected", [
    ("playgrounds", True),
    ("look", False),
    ("Adam", False),
    ("NIOcean", False),  # 'N' і 'n' повинні вважатися однаковими
    ("I Love Mate academy", False),
    ("wrong", True),
    ("brother", True),
    ("Ukraine", True),
    ("", True)
])
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
