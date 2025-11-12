import pytest
from app.main import is_isogram


@pytest.mark.parametrize("input_word,expected", [
    pytest.param("playgrounds", True,
                 id="Should return True if input_word is playgrounds"),
    pytest.param("look", False,
                 id="Should return False if input_word is look"),
    pytest.param("Adam", False,
                 id="Should return False if input_word is Adam"),
    pytest.param("", True,
                 id="Should return True if input_word is empty string"),
])
def test_is_isogram(input_word: str,
                    expected: bool
                    ) -> None:

    assert is_isogram(input_word) == expected
