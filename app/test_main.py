import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, result",
    [
        ("playgrounds", True),
        ("look", False),
        ("Apple", False),
        ("Football", False),
        ("", True)
    ]
)
def test_is_isogram(word: str, result: bool) -> None:
    assert is_isogram(word) == result


@pytest.mark.parametrize(
    "word",
    [
        "TestWord",
        "AnotherWord"
    ]
)
def test_diff_register(word: str) -> None:
    assert not is_isogram(word), (
        "String with different cases of the same letter is not an isogram.")
