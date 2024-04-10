from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "text, expected",
    [
        pytest.param(
            "playgrounds", True,
            id="Word is isogram"
        ),
        pytest.param(
            "hello", False,
            id="Word is not isogram"
        ),
        pytest.param(
            "", True,
            id="Empty string is isogram"
        ),
        pytest.param(
            "underground", False,
            id="The same letter in others index place"
        ),
        pytest.param(
            "Test", False,
            id="Ignore case insensitive"
        )
    ]
)
def test_is_isogram_logic(text: str, expected: bool) -> None:
    assert is_isogram(word=text) == expected
