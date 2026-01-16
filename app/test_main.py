from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word,result",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True)
    ]
)
def test_word_is_not_repeat(word: str, result: bool) -> None:
    result = is_isogram(word)
    assert is_isogram("") is True
    assert is_isogram("Adam") is False
    assert is_isogram("aDaM") is False
    assert is_isogram("abracadabra") is False
    assert is_isogram("paper") is False
    assert is_isogram("playgrounds") is True
    assert is_isogram("lamp") is True
    assert is_isogram("letter") is False
    assert is_isogram("look") is False
    assert isinstance(result, bool)
