import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected_value",
    [
        pytest.param(
            "",
            True,
            id="test_empty_string_is_isogram"
        ),
        pytest.param(
            "playground",
            True,
            id="test_non_consecutive_letters_are_not_isogram"
        ),
        pytest.param(
            "look",
            False,
            id="test_consecutive_letters_are_not_isogram"
        ),
        pytest.param(
            "Adam",
            False,
            id="isogram_is_case_insensitive"
        )
    ]
)
def test_is_isogram(word: str, expected_value: bool) -> None:
    assert is_isogram(word) is expected_value
