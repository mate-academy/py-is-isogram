import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "string, check_bool",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True)
    ]
)
def test_if_isogram_is_correct(string: str, check_bool: bool) -> None:
    assert is_isogram(string) == check_bool
