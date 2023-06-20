from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word,is_iso",
    [
        ("", True),
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("MAma", False),
    ]
)
def test_correctly_is_isogram(
        word: str,
        is_iso: bool
) -> None:
    assert is_isogram(word) == is_iso
