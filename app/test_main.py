import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "word,expected",
    [
        pytest.param("", True, id="test_empty_string_is_isogram"),
        pytest.param("playgrounds", True, id="test_isogram"),
        pytest.param("look", False, id="test_non_isogram"),
        pytest.param("loco", False, id="test_non_consequtive_non_isogram"),
        pytest.param("plaYGrounds", True, id="test_upper_case_letters")
    ]
)
def test_is_isogram(word: str, expected: bool) -> None:
    assert is_isogram(word) == expected


def test_raises_attribute_error() -> None:
    with pytest.raises(AttributeError):
        is_isogram(1)
