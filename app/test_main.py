import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expectation",
    [
        pytest.param("playgrounds", True),
        pytest.param("look", False),
        pytest.param("Adam", False),
        pytest.param("", True),
    ]
)
def test_get_coin_combination(word: str, expectation: bool) -> None:
    assert is_isogram(word) == expectation
