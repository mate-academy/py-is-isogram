import pytest

from app.main import is_isogram

TEST_CASES = [
    pytest.param("playgrounds", True, id="all letters are different"),
    pytest.param("look", False, id="repetitive letters"),
    pytest.param("Adam", False, id="repetitive letters in different cases"),
    pytest.param("", True, id="empty string"),
    pytest.param("a", True, id="single letter"),
    pytest.param("moOse", False, id="repetitive letters in mixed case"),
]


@pytest.mark.parametrize("word,expected", TEST_CASES)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
