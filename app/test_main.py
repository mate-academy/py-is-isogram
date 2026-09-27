import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, result",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("AbcDefgHIjklmnopqrstuvwxyz", True),
        ("AbcDefgHIjklmmnopqrstuvwxyz", False),
        ("aAbcDefgHIjklmnopqrstuvwxyz", False)
    ]
)
def test_is_isogram(word: str, result: bool) -> None:
    actual = is_isogram(word)
    assert (
        is_isogram(word) == result
    ), f"{word} expected result {result} actual {actual}"
