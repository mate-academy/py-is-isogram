from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word,result",
    [
        pytest.param("playgrounds", True),
        pytest.param("look", False),
        pytest.param("Adam", False),
        pytest.param("", True),
    ]
)
def test_all_possible_coin_denominations_are_used(word: str,
                                                  result: bool) -> None:
    assert (result == is_isogram(word))
