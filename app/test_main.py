import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, result",
    [
        pytest.param("", True,
                     id="Test an empty string"),
        pytest.param("playgrounds", True,
                     id="Test an isogram string."),
        pytest.param("look", False,
                     id="Test a non-isogram string."),
        pytest.param("Adam", False,
                     id="Test a non-isogram string(M)")
    ]
)
def test_is_isogram(
        word: str,
        result: bool
) -> None:
    assert (is_isogram(word) == result)
