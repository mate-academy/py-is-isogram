import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected",
    [
        pytest.param(
            "playgrounds", True,
            id="unique letters"
        ),
        pytest.param(
            "look", False,
            id="double letter"
        ),
        pytest.param(
            "Adam", False,
            id="repeated letters with different case"
        ),
        pytest.param(
            "", True,
            id="empty string is isogram"
        ),
        pytest.param(
            "a", True,
            id="single letter is isogram"
        ),
        pytest.param(
            "Aa", False,
            id="case insensitive duplicate"
        ),
        pytest.param(
            "hello", False,
            id="repeated letter"
        ),
        pytest.param(
            "AbCd", True,
            id="unique letters with different case"
        ),
        pytest.param(
            "abca", False,
            id="first letter repeated at the end"
        )
    ],
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
