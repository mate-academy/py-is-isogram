import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word,result",
    [
        ("", True),
        ("latino", True),
        ("PlayGrounds", True),
        ("Adam", False),
        ("loop", False),
    ],
    ids=[
        "test empty string is isogram",
        "test is isogram",
        "test isogram is case-insensitive",
        "test non isogram is case-insensitive",
        "test non isogram",
    ]
)
def test_is_isogram(word: str, result: bool) -> None:
    assert is_isogram(word) == result
