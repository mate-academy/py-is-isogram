from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word, answer",
    [
        pytest.param(
            "playgrounds",
            True,
            id="should return 'True' if word is isogram"
        ),
        pytest.param(
            "look",
            False,
            id="should return 'False' if word is not isogram"
        ),
        pytest.param(
            "Adam",
            False,
            id="should be case-insensitive 'upper' and "
               "'lower' letter are the same"
        ),
        pytest.param(
            "",
            True,
            id="should return 'True' if word is empty string"
        )
    ]
)
def test_is_isogram(word: str, answer: bool) -> None:
    assert is_isogram(word) == answer
