import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, excepted",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("bB", False),
        ("", True),
        (" ", True),
        ("underground", False)
    ]
)
def test_for_is_isogram(word: str, excepted: bool) -> None:
    assert is_isogram(word) == excepted
