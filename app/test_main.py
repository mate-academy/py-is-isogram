import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word_input,result",
    [
        pytest.param("playgrounds", True,
                     id="Test an isogram word."),
        pytest.param("", True,
                     id="Test an empty string."),
        pytest.param("Adam", False,
                     id="Test a non isogram word."),
        pytest.param("look", False,
                     id="Test a non isogram word.")
    ]
)
def test_isogram(word_input: str, result: bool) -> None:
    assert is_isogram(word_input) == result
