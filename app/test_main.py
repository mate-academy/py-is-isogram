import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        pytest.param("playgrounds", True, id="Should pass if word is isogram"),
        pytest.param(
            "Adam",
            False,
            id="Should pass if exist duplicates with different keyboard layout"
        ),
        pytest.param(
            "look",
            False,
            id="Should pass if exist consecutive same letters"
        ),
        pytest.param("", True, id="Should pass if word is empty"),
    ]
)
def test_pass(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
