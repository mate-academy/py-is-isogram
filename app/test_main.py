import pytest

from app.main import is_isogram

@pytest.mark.parametrize(
    "word, result",
    [
        pytest.param(
            "playgrounds",
            True,
            id="function should return True if word is 'playground'"
        ),
        pytest.param(
            "look",
            False,
            id="function should return False if word is 'look'"
        ),
        pytest.param(
            "Adam",
            False,
            id="function should return False if word is 'Adam'"
        ),
        pytest.param(
            "",
            True,
            id="function should return True if word is empty string"
        )
    ]
)
def test_is_isogram(word: str, result: bool) -> None:
    assert is_isogram(word) == result
