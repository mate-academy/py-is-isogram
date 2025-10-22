import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "input_string, expected",
    [
        ("playground", True),
        ("look", False),
        ("Adam", False),
        ("", True),
        ("isogram", True),
        ("hello", False),
        ("Dermatoglyphics", True),
        ("aba", False),
        ("moOse", False),
        ("isIsogram", False),
    ]
)
def test_is_isogram(input_string: str, expected: bool) -> None:
    assert is_isogram(input_string) is expected
