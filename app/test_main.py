from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word, expected",
    [
        ("look", False),
        ("Adam", False),
        ("", True,)
    ],
    ids=[
        "Word shouldn't have repeating letters",
        "Case of letter doesn't mather",
        "Empy word should be `Isogram`"
    ]
)
def test_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
