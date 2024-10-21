from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word, expected_bool", [
        pytest.param(
            "playgrounds", True,
            id="is isogram"
        ),
        pytest.param(
            "", True,
            id="empty string"
        ),
        pytest.param(
            "look", False,
            id="repeating letters"
        ),
        pytest.param(
            "Adam", False,
            id="upper- and lowercase of one letter"
        ),
    ]
)
def test_if_is_isogram(word: str, expected_bool: bool) -> None:
    assert is_isogram(word) == expected_bool
