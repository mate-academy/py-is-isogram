import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected",
    [
        pytest.param("", True),
        pytest.param("Adam", False),
        pytest.param("look", False),
        pytest.param("playgrounds", True)
    ]
)
def test_should_return_bool_value(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected
