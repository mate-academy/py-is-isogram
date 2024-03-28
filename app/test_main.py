import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected_result",
    [
        pytest.param("", True,
                     id="the empty string is an isogram"),
        pytest.param("look", False,
                     id="'look' is not an isogram"),
        pytest.param("Adam", False,
                     id="function should be case-insensitive"),
        pytest.param("playgrounds", True,
                     id="'playgrounds' is an isogram"),
        pytest.param(" ", True,
                     id="gap is an isogram"),
    ]
)
def test_should_return_proper_coin_combination(word: str,
                                               expected_result: list
                                               ) -> None:
    assert is_isogram(word) == expected_result
