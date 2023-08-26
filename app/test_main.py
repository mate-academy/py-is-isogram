import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected_result",
    [
        pytest.param(
            "",
            True,
            id='should return True if value is ""'
        ),
        pytest.param(
            "playgrounds",
            True,
            id="should return True if every element is unique"
        ),
        pytest.param(
            "look",
            False,
            id="should return False if not every element is unique"
        ),
        pytest.param(
            "Adam",
            False,
            id=("should return False even if one element"
                " is uppercase and the same one is lowercase")
        ),
    ]
)
def test_check_word_is_isogram(word: str, expected_result: bool) -> None:
    assert is_isogram(word) == expected_result
