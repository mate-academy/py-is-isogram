import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, result",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True)
    ],
    ids=[
        "No repetitions",
        "1 Repetitive letter",
        "Case insensitivity",
        "Empty string"
    ]
)
def test_all_cases(word: str, result: bool) -> None:
    assert (
        is_isogram(word) == result
    )
