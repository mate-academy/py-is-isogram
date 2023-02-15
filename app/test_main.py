from app.main import is_isogram

import pytest


@pytest.mark.parametrize(
    "word,expected_bool",
    [
        pytest.param(
            "",
            True,
            id="should return true if word is empty"
        ),
        pytest.param(
            "playgrounds",
            True,
            id="should return True if the word does not contain the same letters"
        ),
        pytest.param(
            "Adam",
            False,
            id="should return False if the word contains two letters in different cases"
        ),
        pytest.param(
            "look",
            False,
            id="should return False if the word contains two identical letters"
        )

    ]
)
def test_return_boolean_value_correctly(word: str, expected_bool: bool) -> None:
    assert is_isogram(word) is expected_bool
