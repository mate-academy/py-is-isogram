from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word, result",
    [
        ("a", True),
        ("aa", False),
        ("qwertyuiop", True),
        ("qwertyuiowertyu", False),
        ("", True),
        ("aaD", False),
        ("AaD", False),
    ]
)
def test_is_isogram(word: str, result: bool) -> None:
    assert is_isogram(word) == result, (
        f"Function 'is_isogram' should return {result} "
        f"when word is {word}"
    )
