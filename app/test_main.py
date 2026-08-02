import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected_result",
    [
        pytest.param(
            "",
            True,
            id="Empty string is an isogram."
        ),
        pytest.param(
            "playgrounds",
            True,
            id="Words with no repeating letters are isograms"
        ),
        pytest.param(
            "Playgrounds",
            True,
            id="Words with no repeating capital letters are isograms"
        ),
        pytest.param(
            "look",
            False,
            id="Not only consecutive letters are not an isogram."
        ),
        pytest.param(
            "Adam",
            False,
            id=" String with different cases "
               "of the same letter is not an isogram."
        )
    ]
)
def test_words(
        word: str,
        expected_result: bool
) -> None:
    assert is_isogram(word) == expected_result
