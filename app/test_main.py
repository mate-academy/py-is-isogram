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
        "1",
        "2",
        "3",
        "4"
    ],
)
def test_is_isogram(word: str, result: bool) -> None:
    assert is_isogram(word) == result, (
        f"Results of cheking {word} for isogram is {result}"
    )
