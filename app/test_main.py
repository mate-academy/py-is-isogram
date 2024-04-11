import pytest

from app.main import is_isogram


@pytest.mark.parametrize("word, expected_boolean_value", [
    pytest.param("", True, id="test should return True "
                              "if 'word' is empty"),
    pytest.param("a", True, id="test should return True "
                               "if 'word' has only one letter"),
    pytest.param("aa", False, id="test should return False "
                                 "if 'word' has a duplicate letter"),
    pytest.param("play", True, id="test should return True "
                                  "if 'word' is longer than one letter and "
                                  "there is no repetition of letters"),
    pytest.param("look", False, id="test should return False "
                                   "if inside 'word' two identical letters"),
    pytest.param("Mom", False, id="test should return False "
                                  "if the first and last "
                                  "letters are the same"),
])
def test_is_isogram(word: str, expected_boolean_value: bool) -> None:
    assert (is_isogram(word) == expected_boolean_value)
