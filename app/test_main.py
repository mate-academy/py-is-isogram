from app.main import is_isogram
import pytest


@pytest.mark.parametrize(
    "string,result",
    [
        ("", True),
        ("playgrounds", True),
        ("AdaM", False),
        ("Mm", False),
        ("M", True),
        ("1234567891", False),
        ("#$%^#*()", False)
    ],
    ids=[
        "test empty string",
        "test regular case",
        "test mixed case",
        "test mixed case",
        "test single char",
        "check letters",
        "check symbols"
    ]
)
def test_is_isogram(string: str, result: bool) -> None:
    assert is_isogram(string) is result
