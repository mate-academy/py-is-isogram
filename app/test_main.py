import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, result",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("MaTe", True),
        ("%#$_!", True),
    ],
    ids=[
        "returns True because word isogram",
        "returns because 'oo'",
        "returns False because A upper",
        "str len zero",
        "all str must be lower",
        "element different"
    ]
)
def test_isogram_result(word: str, result: bool) -> None:
    assert is_isogram(word) == result
