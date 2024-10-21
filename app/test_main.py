import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True)
    ],
    ids=[
        "test is isogram",
        "test not isogram",
        "test word with upper letter",
        "test empty word"
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
