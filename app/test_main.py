import pytest

from app.main import is_isogram


@pytest.mark.parametrize("word", [
    pytest.param(""),
    pytest.param("playgrounds"),
    pytest.param("Cents"),
    pytest.param("aBwTq"),
    pytest.param("INSTAL"),
])
def test_is_isogram_true(word: str) -> None:
    assert is_isogram(word)


@pytest.mark.parametrize("word", [
    pytest.param("look"),
    pytest.param("Adam"),
    pytest.param("LIDL"),
    pytest.param("oreo"),
])
def test_is_isogram_false(word: str) -> None:
    assert not is_isogram(word)
