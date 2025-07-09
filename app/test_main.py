from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word, check",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        (" ", True)
    ]
)
def tests_for_func_isogram(word: str, check: bool) -> None:
    assert is_isogram(word) == check
