import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "test_input,expected_bool", [
        ("aaa", False),
        ("", True),
        ("Atest", False),
        ("ITS testing string", False),
        ("aTest", False),
        ("looking", False)
    ]
)
def test_is_program(test_input: str, expected_bool: bool) -> None:
    assert is_isogram(test_input) == expected_bool
