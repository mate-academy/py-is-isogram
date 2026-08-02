from app.main import is_isogram

import pytest


@pytest.mark.parametrize("word, expected_result", [
    pytest.param("isogram", True, id="simple isogram"),
    pytest.param("Alphabet", False, id="mixed case"),
    pytest.param("hello", False, id="not isogram"),
    pytest.param("aba", False, id="duplicate letters"),
    pytest.param("", True, id="empty string"),
    pytest.param(" ", True, id="single space"),
    pytest.param("two words", False, id="multiple words"),
])
def test_is_isogram(word: str, expected_result: bool) -> None:
    assert is_isogram(word) == expected_result
