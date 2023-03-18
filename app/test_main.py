from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word, expected_result",
    [
        ("Playgrounds", True),
        ("Look", False),
        ("Adam", False),
        ("", True),
    ])
def test_is_isogram(word: str, expected_result: bool) -> None:
    assert is_isogram(word) == expected_result
