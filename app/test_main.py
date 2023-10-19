import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, is_an_isogram",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True)
    ]
)
def test_is_isogram(word: str, is_an_isogram: bool) -> None:
    assert is_isogram(word) == is_an_isogram
