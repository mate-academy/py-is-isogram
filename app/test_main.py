from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "word,result",
    [
        pytest.param("", True, id="Test with empty input"),
        pytest.param("PLAYgrounds", True, id="Test with diff-case input"),
        pytest.param("adam", False, id="Test with non-isogram word"),
        pytest.param("Kk", False, id="Test with non-isogram word"),
    ]
)
def test_different_input_data(word: str,
                              result: bool) -> None:
    assert is_isogram(word) == result
