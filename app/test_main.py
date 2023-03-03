import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,result",
    [
        ("", True),
        ("playground", True),
        ("look", False),
        ("Adam", False)
    ],
    ids=[
        "return True for empty string",
        "similar letters",
        "similar letters",
        "similar letters different case"
    ]
)
def test_is_isogram(word: str, result: bool) -> None:
    assert is_isogram(word) is result
