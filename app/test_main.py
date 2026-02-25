from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word,expected",
    [
        pytest.param("playgrounds", True,
                     id="should return True"),
        pytest.param("look", False,
                     id="should return False"),
        pytest.param("Adam", False,
                     id="should return False"),
        pytest.param("", True,
                     id="should return True"),
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected, \
        "should return True or False"
