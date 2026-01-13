import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "string,expected",
    [
        ("", True),
        ("Adam", False),
        ("Look", False),
        ("playgrounds", True),
        ("a", True),
        ("abca", False),
        ("Dermatoglyphics", True),
        ("noon", False),
    ]
)
def test_main(string: str, expected: bool) -> None:
    assert is_isogram(string) == expected
