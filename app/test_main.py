import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word,result",
    [
        pytest.param("", True, id="check_empty"),
        pytest.param("playgrounds", True, id="check_true"),
        pytest.param("Adam", False, id="check_case_sensitivity"),
        pytest.param("look", False, id="check_false"),

    ]
)
def test_get_coins(word: str, result: bool) -> None:
    assert (
        is_isogram(word) == result
    ), f"Is isogram from {word} should be equal to {result}"
