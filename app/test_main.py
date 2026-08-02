import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "init_string, expected_bool",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True)
    ]
)
def test_isogram(init_string: str, expected_bool: bool) -> None:
    assert is_isogram(init_string) == expected_bool
