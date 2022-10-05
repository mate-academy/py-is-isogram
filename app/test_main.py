from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word, expected",
    [
        pytest.param("look", False,),
        pytest.param("Adam", False,),
        pytest.param("playgrounds", True),
        pytest.param("", True,)
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
