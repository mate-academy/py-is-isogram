from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word, expected_result",
    [
        pytest.param("playgrounds", True, id="should return True for isogram"),
        pytest.param(
            "look",
            False,
            id="should return False when same letter is lowercase"
        ),
        pytest.param(
            "Adam",
            False,
            id="should return False when same letter in different cases"
        ),
        pytest.param("", True, id="should return True for an empty line")
    ]
)
def test_is_isogram(word: str, expected_result: bool) -> None:
    assert is_isogram(word) is expected_result
