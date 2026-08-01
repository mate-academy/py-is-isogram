from app.main import is_isogram


import pytest


@pytest.mark.parametrize(
    "word,result",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True)
    ]
)
def test_first(word: str, result: list) -> None:
    assert is_isogram(word) == result
