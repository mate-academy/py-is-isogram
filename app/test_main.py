from app.main import is_isogram
import pytest


@pytest.mark.parametrize("word,isogram",
                         [pytest.param("playgrounds", True),
                          pytest.param("", True)])
def test_is_isogram(word: str, isogram: bool) -> None:
    assert is_isogram(word) == isogram


@pytest.mark.parametrize("word,not_isogram",
                         [pytest.param("look", False),
                          pytest.param("Adam", False)])
def test_is_not_isogram(word: str, not_isogram: bool) -> None:
    assert is_isogram(word) == not_isogram
