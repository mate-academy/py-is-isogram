import pytest
from app.main import is_isogram


@pytest.mark.parametrize(
    "string,expected",
    [
        ("aloha", False),
        ("bye", True),
        ("Hah", False),
        ("", True)
    ],
    ids=[
        "`aloha` should return `False`",
        "`bye` should return `True`",
        "`Hah` should return `False`",
        "empty string should return `True`"
    ]
)
def test_should_return_correct_value(string: str,
                                     expected: bool) -> None:
    assert is_isogram(string) == expected
