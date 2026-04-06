import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, result",
    [
        pytest.param(
            "playgrounds",
            True,
            id="test playgrounds"
        ),
        pytest.param(
            "look",
            False,
            id="test look"
        ),
        pytest.param(
            "Adam",
            False,
            id="test Adam"
        ),
        pytest.param(
            "",
            True,
            id="test empty string"
        )
    ]
)
def test_on_no_repeating_letters(word: str, result: bool) -> None:
    assert is_isogram(word) == result
