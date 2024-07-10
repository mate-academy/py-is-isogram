import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, result",
    [
        ("", True),
        ("a", True),
        ("Adam", False),
        ("Look", False),
        ("playgrounds", True)
    ], ids=["empty", "single", "double", "Too oo", "long isogram"]
)
def test_is_isogram(word: str, result: bool) -> None:
    assert is_isogram(word) == result
