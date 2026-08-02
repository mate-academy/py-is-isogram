from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word,result",
    [
        pytest.param(
            "playgrounds",
            True,
            id="test if letters are not dublicated"
        ),
        pytest.param(
            "look",
            False,
            id="test if letters are dublicated"
        ),
        pytest.param(
            "Adam",
            False,
            id="should ignore upper case"
        ),
        pytest.param(
            "",
            True,
            id="empty string must be isogram"
        )
    ]
)
def test_is_isogram(word: str, result: bool):
    assert is_isogram(word) is result
