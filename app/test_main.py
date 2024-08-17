from app.main import is_isogram

import pytest


@pytest.mark.parametrize(
    "word,expected",
    [
        pytest.param(
            "",
            True,
            id="checking edge cases"
        ),
        pytest.param(
            "Miracle",
            True,
            id="checking edge cases"
        ),
        pytest.param(
            "Mom",
            False,
            id="checking edge cases"
        ),
        pytest.param(
            "Adam",
            False,
            id="checking edge cases"
        ),
        pytest.param(
            "playgrounds",
            True,
            id="checking edge cases"
        ),
        pytest.param(
            "qwertyuiopasdfghjklzxcvbnm",
            True,
            id="checking edge cases"
        ),
        pytest.param(
            "qwertyuiopasdfghjklzxcvbnmQ",
            False,
            id="checking edge cases"
        ),
    ]
)
def test_universal(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
