import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,result",
    [
        pytest.param("playgrounds", True),
        pytest.param("look", False),
        pytest.param("Adam", False),
        pytest.param("", True),
    ]
)
def test_is_isogram(word: str, result: bool) -> None:
    assert is_isogram(word) == result, \
        "Not expected result"
