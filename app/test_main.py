import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected",
    [
        pytest.param("playgrounds", True),
        pytest.param(" ", True),
        pytest.param("", True),
        pytest.param("look", False),
        pytest.param("Adam", False),
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected


@pytest.mark.parametrize(
    "word,error",
    [
        pytest.param(13, TypeError),
        pytest.param(["wef"], TypeError),
        pytest.param([324], TypeError),
    ]
)
def test_error_is_isogram(word: str, error: type[Exception]) -> None:
    with pytest.raises(error):
        if type(word) != str:
            raise error
