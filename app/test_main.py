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
        "word with unique letters",
        "word with double letter",
        "word with uppercase",
        "empty string"
    ]
)
def test_method(word: str, result: bool) -> None:
    assert is_isogram(word) == result
