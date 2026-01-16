from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word, isiso",
    [
        ("", True),
        ("playgrounds", True),
        ("Look", False),
        ("Milk", True),
        ("Mimik", False),
        ("Cadic", False),
        ("AAAAA", False),
        ("eeee", False)
    ]
)
def test_is_isogram(word: str, isiso: bool) -> None:
    assert is_isogram(word) == isiso
