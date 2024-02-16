import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected_result",
    [
        pytest.param(
            "", True,
            id="should return True for empty string"
        ),
        pytest.param(
            "abc", True,
            id="should return True for if string is isogram"
        ),
        pytest.param(
            "abca", False,
            id="should return False for if string is not isogram"
        ),
        pytest.param(
            "a b c", False,
            id="should work with spaces"
        ),
        pytest.param(
            "Abca", False,
            id="should work with uppercase letters"
        ),
    ]
)
def test_is_isogram(word: str, expected_result: bool) -> None:
    result = is_isogram(word)

    assert result == expected_result
