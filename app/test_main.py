import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        pytest.param(
            "",
            True,
            id="empty word"
        ),
        pytest.param(
            "w",
            True,
            id="one letter word"
        ),
        pytest.param(
            "Adam",
            False,
            id="lower- and uppercase letter in word"
        ),
        pytest.param(
            "look",
            False,
            id="2 same letters in word"
        ),
        pytest.param(
            "playgrounds",
            True,
            id="long word"
        )
    ]
)
def test_is_isogram(word, expected):
    assert is_isogram(word) == expected
