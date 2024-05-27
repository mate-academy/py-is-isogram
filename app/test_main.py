import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected_result",
    [
        pytest.param(
            "playgrounds",
            True,
            id="should return True when word is isogram"
        ),
        pytest.param(
            "look",
            False,
            id="should return False when word is not isogram"
        ),
        pytest.param(
            "",
            True,
            id="should return True when empty string"
        ),
        pytest.param(
            "Adam",
            False,
            id="should return False when same letters in different case"
        ),
    ]
)
def test_is_isogram(word: str, expected_result: bool) -> None:
    assert is_isogram(word) == expected_result
