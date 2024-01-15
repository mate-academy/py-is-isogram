import pytest

from app.main import is_isogram

@pytest.mark.parametrize(
    "word,result",
    [
        pytest.param("playgrounds", True, id="playground is isogram"),
        pytest.param("", True, id="Empty string is isogram"),
        pytest.param("look", False, id="Look is not an isogram"),
        pytest.param("Adam", False, id="Isogram is case-insensitive"),
    ]
)
def test_coin_combinations(word: str, result: bool) -> None:
    assert (
        is_isogram(word) == result
    ), f"{word} is not an isogram"
