import pytest
from app.main import is_isogram


@pytest.mark.parametrize("word, expected", [
    ("playgrounds", True),
    ("look", False),
    ("Adam", False),
    ("", True),
    ("AAAAAA", False),
    ("cccccc", False),
    ("abracadabra", False)
])
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected


@pytest.mark.parametrize("word", [
    1,
    90.3,
    None
])
def test_should_return_type_error_for_invalid_type(
        word: int | float | None
) -> None:
    with pytest.raises(TypeError) as e:
        is_isogram(word)
    assert str(e.value) == f"'{word}' is not a string"
