import pytest
from app.main import is_isogram


# write your code here
@pytest.mark.parametrize(
    "word, result",
    [
        pytest.param("playgrounds", True, id="check word 'playgrounds'"),
        pytest.param("look", False, id="check word 'look'"),
        pytest.param("Adam", False, id="check word 'Adam'"),
        pytest.param("", True, id="check empty string")
    ])
def test_check_words(word: str, result: bool) -> None:
    assert is_isogram(word) == result
