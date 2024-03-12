from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word,expected_result",
    [
        pytest.param("aaa", False),
        pytest.param("", True),
        pytest.param("playgrounds", True),
        pytest.param("look", False),
        pytest.param("Adam", False),
    ]
)
def test_is_isogram(
        word: str,
        expected_result: bool) -> None:
    assert is_isogram(word) == expected_result
