from app.main import is_isogram

import pytest


@pytest.mark.parametrize("words, expected", [
    pytest.param("", True, id="empty"),
    pytest.param("playgrounds", True, id="playgrounds"),
    pytest.param("look", False, id="look"),
    pytest.param("Adam", False, id="Adam"),
])
def test_is_isogram(words: str, expected: bool) -> None:
    assert is_isogram(words) is expected
