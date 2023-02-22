import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected_result",
    [
        pytest.param("playgrounds", True, id="test with different words"),
        pytest.param("look", False, id="test with not different words"),
        pytest.param("Adam", False, id="test with same letter"),
        pytest.param("", True, id="test with empty string"),

    ]
)
def test_function_is_isogram(
        word: str,
        expected_result: bool
) -> bool:
    assert is_isogram(word) == expected_result
