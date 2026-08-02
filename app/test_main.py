import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected_result",
    [
        pytest.param(
            "",
            True,
            id="Should return True if word is empty"
        ),
        pytest.param(
            "Adam",
            False,
            id="test if word contains repeating letters with different case"
        ),
        pytest.param(
            "look",
            False,
            id="test if word contains repeating letters"
        ),
        pytest.param(
            "playgrounds",
            True,
            id="test if words not contains repeating letters"
        )
    ]
)
def test_repeating_letters(word: str, expected_result: bool) -> None:
    assert is_isogram(word) == expected_result
