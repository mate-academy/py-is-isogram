from app.main import is_isogram

import pytest


@pytest.mark.parametrize(
    "word, result",
    [
        pytest.param("", True, id="test_empty_string"),
        pytest.param("cup", True, id="test_correct_isogram"),
        pytest.param("Faanta", False, id="test_not_isogram"),
        pytest.param("AbsoLutely", False,
                     id="test_not_isogram_case_insensative"),
    ]
)
def test_is_isogram(word: str, result: bool) -> None:
    assert is_isogram(word) == result
