import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, result",
    [
        pytest.param(
            "playgrounds", True,
            id="result_have_to_be_correct"
        ),
        pytest.param(
            "look", False,
            id="result_have_to_be_correct"
        ),
        pytest.param(
            "Adam", False,
            id="function_should_be_case-insensitive"
        ),
        pytest.param(
            "", True,
            id="empty_string_is_isogram"
        ),
    ]
)
def test_correct_result(word: str, result: bool) -> None:
    assert is_isogram(word) == result
