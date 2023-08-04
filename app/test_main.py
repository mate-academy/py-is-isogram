import pytest

from app.main import is_isogram


# write your code here
@pytest.mark.parametrize(
    "word, result",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True)
    ]
)
def test_is_isogram(word: str, result: bool) -> None:
    assert (
            is_isogram(word) == result
    )
