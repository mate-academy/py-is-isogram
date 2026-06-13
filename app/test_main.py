import pytest

from app.main import is_isogram


@pytest.mark.parametrize("word, expected", [
    pytest.param(
        "playgrounds", True,
        id="should return True when is isogram"
    ),
    pytest.param(
        "look", False,
        id="should return False because of two 'o'"
    ),
    pytest.param(
        "Adam", False,
        id="should return False because of two 'a' in different register"
    ),
    pytest.param(
        "", True,
        id="should return True for empty string"
    ),
])
def test_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
