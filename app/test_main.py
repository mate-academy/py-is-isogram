import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, result",
    [
        pytest.param(
            "playgrounds",
            True,
            id="must return True if word is isogram"
        ),
        pytest.param(
            "look",
            False,
            id="must return false if word nor isogram"
        ),
        pytest.param(
            "Adam",
            False,
            id="must return False if count letter more than 1"
        ),
        pytest.param(
            "",
            True,
            id="must return True if word is empty"
        )
    ]
)
def test_word_isogram_true_or_false(
        word: str,
        result: bool
) -> None:
    assert is_isogram(word) == result
