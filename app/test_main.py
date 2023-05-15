import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "input_word, result",
    [
        pytest.param("playgrounds", True),
        pytest.param("look", False),
        pytest.param("Adam", False),
        pytest.param("", True)
    ]
)
def test_is_isogram(input_word: str, result: bool) -> None:
    assert is_isogram(input_word) == result
