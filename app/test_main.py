from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word, result",
    [
        ("", True),
        ("Adam", False),
        ("look", False),
        ("isogram", True),
        ("playground", True)
    ]
)
def test_main(word: str, result: bool) -> None:
    assert is_isogram(word) == result
