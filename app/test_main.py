import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "string, expected",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("Alphabet", False),
        ("isogram", True),
        ("moose", False),
        ("subdermatoglyphic", True),
    ]
)
def test_if_string_is_isogram(string: str, expected: bool) -> None:
    assert is_isogram(string) is expected


@pytest.mark.parametrize(
    "invalid_input",
    [
        567,
        -234,
        True,
        False
    ]
)
def test_type_value(invalid_input: any) -> None:
    with pytest.raises(TypeError):
        is_isogram(invalid_input)
