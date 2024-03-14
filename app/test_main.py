import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "string_word, result",
    [
        pytest.param(
            "playgrounds",
            True,
            id="test return True of 'playgrounds'"
        ),
        pytest.param(
            "look",
            False,
            id="test return False of 'look'"
        ),
        pytest.param(
            "Adam",
            False,
            id="test return False of 'Adam'"
        ),
        pytest.param(
            "",
            True,
            id="test return True of Empty string"
        )
    ]
)
def test_is_isogram(string_word: str, result: bool) -> bool:
    assert is_isogram(string_word) == result
