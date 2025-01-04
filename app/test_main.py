from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word, bool_answer",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam'", False),
        ("", True)
    ]
)
def test_is_isogram(
        word: str,
        bool_answer: bool
) -> None:
    assert is_isogram(word) == bool_answer
