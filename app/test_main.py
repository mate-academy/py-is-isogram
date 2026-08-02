from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "init_word, expected_result",
    [
        pytest.param("Adam", False, id="check 'Adam'"),
        pytest.param("look", False, id="check 'look'"),
        pytest.param("AaAa", False, id="check 'AaAa'"),
        pytest.param("A", True, id="check 'A'"),
        pytest.param("playground", True, id="check 'playground'"),
        pytest.param("", True, id="check ''"),
    ]
)
def test_is_isogram(init_word: str, expected_result: bool) -> None:
    result = is_isogram(init_word)
    assert result == expected_result
