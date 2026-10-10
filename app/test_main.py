import pytest


from app.main import is_isogram


@pytest.mark.parametrize(
    "word",
    (
        [""]
    )
)
def test_if_empty_is_isogram(word: str) -> None:
    assert is_isogram(word) is True


@pytest.mark.parametrize(
    "word, result",
    (
        ["playground", True],
        ["look", False],
        ["telegram", False],
        ["bOok", False],
        ["Adam", False],
    )
)
def test_core_of_is_isogram_function(word: str, result: bool) -> None:
    assert is_isogram(word) == result
