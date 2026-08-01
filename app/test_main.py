import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected_output",
    [
        pytest.param(
            "playgrounds",
            True,
            id="test should check if isogram word"
        ),
        pytest.param(
            "look",
            False,
            id="test should check if non isogram word"
        ),
        pytest.param(
            "Adam",
            False,
            id="test should check if isogram word case-insensitive"
        ),
        pytest.param(
            "",
            True,
            id="test should check if empty string is an isogram"
        ),
    ]
)
def test_is_isogram(word: str, expected_output: bool) -> None:
    assert is_isogram(word) == expected_output
