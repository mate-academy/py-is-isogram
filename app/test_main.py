import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word,result", [
        pytest.param("abBy", False, id="mixed case"),
        pytest.param("", True, id="empty string"),
        pytest.param("qwerty", True, id="lowercase isogram"),
        pytest.param("assure", False, id="consecutive same letters"),
        pytest.param("parmigano", False, id="non-consecutive same letters")
    ]
)
def test_correct_bool_result(word: str, result: bool) -> None:
    assert is_isogram(word) == result, "incorrect result"
