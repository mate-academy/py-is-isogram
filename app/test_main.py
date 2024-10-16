import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected",
    [
        pytest.param("playgrounds", True,
                     id="Isogram - 'playgrounds'"),
        pytest.param("look", False,
                     id="Not an isogram - 'look'"),
        pytest.param("Adam", False,
                     id="Not an isogram - 'Adam' (case-insensitive)"),
        pytest.param("", True,
                     id="Empty string is an isogram"),
        pytest.param("isogram", True,
                     id="Isogram - 'isogram'"),
        pytest.param("hello", False,
                     id="Not an isogram - 'hello'"),
        pytest.param("abcdefg", True,
                     id="Isogram - 'abcdefg'"),
        pytest.param("Dermatoglyphics", True,
                     id="Isogram - 'Dermatoglyphics' (case-insensitive)"),
        pytest.param("aba", False,
                     id="Not an isogram - 'aba'"),
        pytest.param("Isogram", True,
                     id="Isogram - 'Isogram' (case-insensitive)"),
        pytest.param("Six-year-old", False,
                     id="Not an isogram - with hyphen"),
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    """Test is_isogram function with various inputs."""
    assert is_isogram(word) == expected
