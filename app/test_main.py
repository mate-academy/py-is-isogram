from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "input_value, output",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("Mom", False)
    ]
)
def test_is_isogram(input_value: str, output: bool) -> None:
    assert is_isogram(input_value) == output


@pytest.mark.parametrize(
    "input_value",
    [
        (1),
        ([1]),
        (True),
        (None),
    ],
    ids=[
        "int",
        "list",
        "bool",
        "none"
    ]
)
def test_check_correct_type(input_value: None) -> None:
    with pytest.raises(AttributeError):
        is_isogram(input_value)
