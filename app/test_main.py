from app.main import is_isogram
import pytest
from typing import Any


@pytest.mark.parametrize(
    "world,expected",
    [
        ("", True),
        ("use", True),
        ("Playground", True),
        ("123456789", True),
        ("SOMEworld", False),
        ("eye", False),
        ("Alpha", False),
        ("  ", False),

    ]
)
def test_is_isogram(world: str, expected: bool) -> None:
    assert is_isogram(world) == expected


@pytest.mark.parametrize(
    "world,expected",
    [
        (150, AttributeError),
        ({"key": "value"}, AttributeError),
        ([1, 2, 3], AttributeError),
        (True, AttributeError),
        (None, AttributeError)
    ]
)
def test_should_raise_errors(world: Any,
                             expected: Exception) -> None:
    with pytest.raises(expected):
        is_isogram(world)
