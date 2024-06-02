import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expect",
    [
        pytest.param(
            "playgrounds",
            True,
            id="test return True for isogram word"
        ),
        pytest.param(
            "look",
            False,
            id="test return False for not isogram word"
        ),
        pytest.param(
            "Adam",
            False,
            id="test return False for not isogram word"
        ),
        pytest.param(
            "",
            True,
            id="test return True for not word"
        ),
    ]
)
def test_check_is_isogram(word: str, expect: bool) -> None:
    assert is_isogram(word) == expect
