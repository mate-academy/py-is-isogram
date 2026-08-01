import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected",
    [
        (
            "secret",
            False,
        ),
        (
            "",
            True
        ),
        (
            "Ccerty",
            False
        ),
        (
            "Certy",
            True
        ),
        (
            "closings",
            False
        ),
        (
            "12345",
            True
        ),
        (
            "112345",
            False
        )
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
