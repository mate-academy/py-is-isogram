import pytest
from app import main


@pytest.mark.parametrize("string,expected", [
    ("playgrounds", True),
    ("look", False),
    ("Adam", False),
    ("Aa", False),
    ("", True),
    ("ABCD", True),
    ("EFGH", True),
    ("IJKL", True),
    ("MNOP", True),
    ("QRSTU", True),
    ("VWXYZ", True)
])
def test_is_isogram(string: str, expected: str) -> str:
    assert main.is_isogram(string) is expected


@pytest.mark.parametrize(
    "invalid_input",
    [
        15,
        1.5,
        None,
        ["a", "b", "c"],
    ]
)
def test_is_isogram_invalid_types(invalid_input: str) -> None:
    with pytest.raises((TypeError, ValueError, AttributeError)):
        main.is_isogram(invalid_input)
