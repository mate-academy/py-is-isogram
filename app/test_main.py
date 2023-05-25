import pytest
from app.main import is_isogram


# write your code here
def test_if_empty_is_isogram() -> None:
    assert is_isogram("") is True


def test_if_case_insensitive_is_isogram() -> None:
    assert is_isogram("Aa") is False


@pytest.mark.parametrize(
    "word, result",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
    ],
    ids=["all dif low case",
         "duplicate low case",
         "duplicate dif case"],
)
def test_dif_examples(word: str, result: bool) -> None:
    assert is_isogram(word) == result
