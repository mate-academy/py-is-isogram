import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected_output",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
    ],
    ids=[
        "word_playgrounds",
        "word_look",
        "word_Adam",
        "word_empty",
    ]
)
def test_is_isogram(word: str, expected_output: bool) -> None:
    assert is_isogram(word) == expected_output
