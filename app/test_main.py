from app.main import is_isogram
import pytest


@pytest.mark.parametrize("word, result",
                         [
                             ("Abba", False),
                             ("", True),
                             (1, AttributeError),
                             ("playgrounds", True),
                             ("Adam", False)
                         ],
                         ids=[
                             "abba must return False",
                             "empty string must be True",
                             "if must return TypeError",
                             "playgrounds must return True",
                             "non consecutive letters are not isogram"
                         ]
                         )
def test_is_isogram(word: str, result: bool | TypeError) -> None:
    if isinstance(result, type) and issubclass(result, Exception):
        with pytest.raises(result):
            is_isogram(word)
    else:
        assert is_isogram(word) == result
