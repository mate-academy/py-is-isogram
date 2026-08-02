import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, categorical",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True)
    ],
    ids=[
        "small_letters",
        "repetition",
        "big_letters",
        "empty_string"
    ]
)
def test_check_all_possibilities(word: str, categorical: bool) -> None:
    assert is_isogram(word) == categorical
