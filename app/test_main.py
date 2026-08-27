import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        pytest.param(
            "",
            True,
            id="empty string is isogram"
        ),
        pytest.param(
            "a",
            True,
            id="single character is isogram"
        ),
        pytest.param(
            "Adam",
            False,
            id="function is case insensitive"
        ),
        pytest.param(
            "qwerty",
            True,
            id="common isogram"
        ),
        pytest.param(
            "aba",
            False,
            id="common non-isogram"
        ),
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
