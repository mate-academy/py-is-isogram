import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        (
            "",
            True
        ),
        (
            "play",
            True
        ),
        (
            "adam",
            False
        ),
        (
            "Adam",
            False
        ),
        (
            "look",
            False
        )
    ]
)
def test_bound_values(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
