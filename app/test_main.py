import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word,result",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True)
    ],
    ids=[
        "Checking isogram word",
        "Checking not isogram word",
        "Checking case-insensitiveness",
        "Checking empty string"
    ]
)
def test_is_isogram(word: str, result: bool) -> None:
    assert is_isogram(word) == result
