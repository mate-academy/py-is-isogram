import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "text,result",
    [
        ("playgrounds", True),
        ("look", False),
        ("Adam", False),
        ("", True)
    ]
)
def test_func_is_isogram(
        text: str,
        result: bool
) -> None:
    assert is_isogram(text) == result
