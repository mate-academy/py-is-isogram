from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word,expected",
    [
        pytest.param("playgrounds", True, id="test playgrounds"),
        pytest.param("", True, id="test empty string"),
        pytest.param("look", False, id="test look"),
        pytest.param("Adam", False, id="test Adam"),
    ]
)
def test_is_isogram(
        word: str,
        expected: bool
) -> None:
    assert is_isogram(word) == expected


@pytest.mark.parametrize(
    "word,expected_error",
    [
        pytest.param(1, AttributeError, id="test input integer"),
    ]
)
def test_errors(
        word: str,
        expected_error: Exception
) -> None:
    with pytest.raises(expected_error):
        is_isogram(word)
