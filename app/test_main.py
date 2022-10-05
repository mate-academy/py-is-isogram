import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, is_true",
    [
        pytest.param(
            "", True,
            id="test should return True when word is empty"
        ),
        pytest.param(
            "h", True,
            id="test should return True when word length == 1"
        ),
        pytest.param(
            "Adam", False,
            id="test should return False when word has same letter in different case"
        ),
        pytest.param(
            "look", False,
            id="test should return False when words has same letter in same case"
        )
    ]
)
def test_should_return_is_isogram(word: str, is_true: bool) -> None:
    assert is_isogram(word) == is_true
