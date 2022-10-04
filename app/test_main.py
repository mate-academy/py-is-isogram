import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        pytest.param(
            "", True,
            id="Return True if input string is empty"
        ),
        pytest.param(
            "look", False,
            id="Return False if repeating letters are consecutive"
        ),
        pytest.param(
            "Firefly", False,
            id="Return False if repeating letters are in different cases"
        )
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
