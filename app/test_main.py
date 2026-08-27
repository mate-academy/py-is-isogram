import pytest

from app import main


@pytest.mark.parametrize(
    "word, expected", [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("AsDfGhJkL", True)
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert (
        main.is_isogram(word) == expected
    ), "Test should return if isogram"
