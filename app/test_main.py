from app.main import is_isogram
import pytest


@pytest.mark.parametrize("word, expected_result", [
    pytest.param(
        "",
        True,
        id="should return True for the empty str"
    ),
    pytest.param(
        "playgrounds",
        True,
        id="should return True if no repeating letters"
    ),
    pytest.param(
        "Yellow",
        False,
        id="should return True for repeating letters"
    ),
    pytest.param(
        "laptop",
        False,
        id="should return True for repeating letters"
    ),
    pytest.param(
        "laptoP",
        False,
        id="should return True for repeating letters"
    ),
])
def test_is_isogram_result(word: str, expected_result: bool) -> None:
    assert is_isogram(word) is expected_result
