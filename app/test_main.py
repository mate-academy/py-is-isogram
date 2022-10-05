import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        pytest.param(
            "playgrounds",
            True,
            id="should return `True` if a word has no repeating letters"
        ),
        pytest.param(
            "look",
            False,
            id="should return `False` if a word has repeating letters"
        ),
        pytest.param(
            "Adam",
            False,
            id="should return `False` if a word has repeating letters"
        ),
        pytest.param(
            "",
            True,
            id="should return `True` for an empty string"
        ),
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
