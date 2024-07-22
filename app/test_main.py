from app.main import is_isogram
from typing import Any
import pytest


@pytest.mark.parametrize(
    "word, expected_result",
    [
        ("", True),
        ("play", True),
        ("Play", True),
        ("Playp", False)

    ]
)
def test_is_iogram(word: str, expected_result: bool) -> None:
    assert is_isogram(word) == expected_result


@pytest.mark.parametrize(
    "word, exception",
    [
        ([], AttributeError),
        ({}, AttributeError)
    ]
)
def test_fro_correct_values(word: Any, exception: AttributeError) -> None:
    with pytest.raises(AttributeError):
        is_isogram(word)
