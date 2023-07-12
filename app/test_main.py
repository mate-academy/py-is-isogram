import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected_result",
    [
        pytest.param(
            "",
            True,
            id="empty string is an isogram"
        ),
        pytest.param(
            "look",
            False,
            id="consecutive letters are not isogram"
        ),
        pytest.param(
            "Adam",
            False,
            id="non consecutive letters are not isogram case insensitive"
        ),
    ]
)
def test_correct_isogram_definition(
        word: str,
        expected_result: bool
) -> None:
    assert is_isogram(word) == expected_result
