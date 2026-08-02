import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected",
    [
        pytest.param(
            "playgrounds",
            True,
            id="Check for unique characters"
        ),
        pytest.param(
            "look",
            False,
            id="Check for duplicate characters"
        ),
        pytest.param(
            "Adam",
            False,
            id="Check uppercase and lowercase"
        ),
        pytest.param(
            "",
            True,
            id="Checking for an empty string"
        ),
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
