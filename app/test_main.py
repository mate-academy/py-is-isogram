import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected_result",
    [
        pytest.param("playgrounds", True, id="playgrounds"),
        pytest.param("look", False, id="look"),
        pytest.param("Adam", False, id="Adam"),
        pytest.param("", True, id="Empty string")
    ]
)
def test_is_isogram_with(word: str, expected_result: bool) -> None:
    test_result = is_isogram(word)
    assert isinstance(test_result, bool)
    assert test_result == expected_result
