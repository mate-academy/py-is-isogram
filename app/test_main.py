import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "test_word,expected_result",
    [
        pytest.param(
            "",
            True,
            id="should return true for empty string"
        ),
        pytest.param(
            "word",
            True,
            id="should return true for word 'word'"
        ),
        pytest.param(
            "wood",
            False,
            id="should return false for word 'wood'"
        ),
        pytest.param(
            "woOd",
            False,
            id="should return false for word 'woOd'"
        ),
        pytest.param(
            "wOOd",
            False,
            id="should return false for word 'wOOd'"
        ),
        pytest.param(
            "people",
            False,
            id="should return false for word 'people'"
        ),
        pytest.param(
            "People",
            False,
            id="should return false for word 'People'"
        ),
        pytest.param(
            "PeoPle",
            False,
            id="should return false for word 'PeoPle'"
        ),
    ]
)
def test_is_isogram(test_word: str, expected_result: bool) -> None:
    assert is_isogram(test_word) == expected_result
