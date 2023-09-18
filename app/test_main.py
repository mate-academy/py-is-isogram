import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, result",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True)
    ],
    ids=[
        "normal isogram",
        "not isogram (all lower case)",
        "not isogram (same letter lower and upper case)",
        "empty string is an isogram"
    ]
)
def test_detecting_isogram_correctly(word: str, result: bool) -> None:
    assert is_isogram(word) == result
