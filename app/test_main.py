import pytest
from app.main import is_isogram


@pytest.mark.parametrize("word, expected", [
    pytest.param("playgrounds", True, id="playgrounds_is_isogram"),
    pytest.param("look", False, id="look_is_not_isogram"),
    pytest.param("Adam", False, id="Adam_is_not_isogram"),
    pytest.param("", True, id="empty_string_is_isogram"),
    pytest.param("zebra", True, id="zebra_is_isogram"),
    pytest.param("alphabet", False, id="alphabet_is_not_isogram"),
    pytest.param("HeLLo", False, id="HeLLo_is_not_isogram"),
])
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
