import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "input_str, expected", [
        ("", True),
        (" ", True),
        ("    ", False),
        ("playground", True),
        ("Adam", False),
        ("look", False),
        ("123", True),
        ("1 2 3", False),
        ("1 22", False),
    ],
    ids=[
        "'' == is True",
        "' ' == is True",
        "'    ' == is False",
        "playground == is True",
        "Adam == is False",
        "look == is False",
        "123 == is True",
        "1 2 3 == is False",
        "1 22 == is False"
    ]
)
def test_for_isogram(input_str: str, expected: bool) -> None:
    assert is_isogram(input_str) == expected
