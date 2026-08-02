import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,result",
    [
        pytest.param("Adam", False, id="lower and upper case"),
        pytest.param("playgrounds", True, id="isogram"),
        pytest.param("look", False, id="non isogram"),
        pytest.param("", True, id="empty")
    ]
)
def test_should_return_bool(word: str, result: bool) -> None:
    assert is_isogram(word) == result
