import pytest

from app.main import is_isogram


@pytest.mark.parametrize("word, expected", [
    pytest.param("playgrounds", True),
    pytest.param("look", False, id="should not"
                                   " be the same letters in the word"),
    pytest.param("", True),
    pytest.param("Adam", False, id="should not"
                                   " be the same letters in the word")
])
def test_should_return_actually_result(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
