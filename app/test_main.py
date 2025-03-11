import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected_result",
    [
        pytest.param("playgrounds", True, id="test_playgrounds"),
        pytest.param("look", False, id="test_look"),
        pytest.param("Adam", False, id="test_adam"),
        pytest.param("", True, id="test_''"),
    ]
)
def test_is_isogram(word: str, expected_result: bool) -> None:
    assert is_isogram(word) is expected_result
