from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word,expected",
    [
        pytest.param(
            "playgrounds",
            True,
            id="should return true for word 'playgrounds'"
        ),
        pytest.param(
            "look",
            False,
            id="should return false for word 'look'"
        ),
        pytest.param(
            "Adam",
            False,
            id="should return false for word 'Adam'"
        ),
        pytest.param(
            "",
            True,
            id="should return true for word ''"
        ),
        pytest.param(
            "ABRACADabra",
            False,
            id="should return false for word 'ABRACADabra'"
        ),
        pytest.param(
            "azbuka",
            False,
            id="should return false for word 'azbuka'"
        )
    ]
)
def test_should_check_word_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
