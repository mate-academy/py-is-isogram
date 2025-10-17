import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "value,bool_value",
    [
        ("", True),
        ("Aang", False),
        ("Zuko", True),
        ("asserts", False),
        ("garage", False)
    ]
)
def test_is_isogram(
        value: str,
        bool_value: bool

) -> None:
    assert is_isogram(value) == bool_value
