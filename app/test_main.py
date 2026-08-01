import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "initial_meaning_word, expected_result",
    [
        pytest.param(
            "",
            True,
        ),

        pytest.param(
            "love",
            True,
        ),

        pytest.param(
            "Adam",
            False,
        ),

        pytest.param(
            "baal",
            False,
        ),
    ]
)
def test_is_isogram(initial_meaning_word: str, expected_result: bool) -> None:
    assert is_isogram(initial_meaning_word) == expected_result
