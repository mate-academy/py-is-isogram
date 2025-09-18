from app.main import is_isogram
import pytest


@pytest.mark.parametrize("word,expected", [
    ("playgrounds", True),
    ("look", False),
    ("Adam", False),
    ("", True)
])
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected

def test_is_isogram_str() -> None:
    with pytest.raises(TypeError):
        is_isogram(0)
    with pytest.raises(TypeError):
        is_isogram(None)
    with pytest.raises(TypeError):
        is_isogram(2.5)
    with pytest.raises(TypeError):
        is_isogram(['a', 'b'])
    with pytest.raises(TypeError):
        is_isogram(True)